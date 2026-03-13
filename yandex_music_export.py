import math
import os
import time
from typing import List, Dict, Any

import pandas as pd
from dotenv import find_dotenv, load_dotenv, set_key
from selenium import webdriver
from yandex_music import Client

OAUTH_URL = (
    "https://oauth.yandex.ru/authorize?"
    "response_type=token&client_id=23cabbbdc6cd418abb4b39c32c41195d"
)
ARTIST_COLUMN = "Artist"
TRACK_COLUMN = "Track Name"
ALBUM_COLUMN = "Album"
TRACK_ID_COLUMN = "Track ID"
ALBUM_ID_COLUMN = "Album ID"
ARTIST_ID_COLUMN = "Artist ID"


def get_yandex_token() -> str:
    env_path = find_dotenv()

    if env_path:
        load_dotenv(env_path)
        token = os.getenv("TOKEN")
        if token:
            return token
    else:
        env_path = ".env"

    driver = webdriver.Chrome()
    driver.get(OAUTH_URL)

    token = None
    while not token:
        current_url = driver.current_url
        if "access_token=" in current_url:
            token = current_url.split("access_token=")[1].split("&")[0]
        time.sleep(1)

    driver.quit()

    if not token:
        raise RuntimeError("Не удалось получить токен")

    set_key(env_path, "TOKEN", token)
    return token


class YandexMusicExporter:
    """Exports liked and disliked music entities."""
    def __init__(self, token: str):
        self.client = Client(token).init()

    @staticmethod
    def _save_csv(rows: List[Dict[str, Any]], filename: str, sort_column: str, chunk_size: int = 500) -> None:
        """Save rows to CSV files split into chunks of max `chunk_size` rows."""

        dataframe = pd.DataFrame(rows)

        if not dataframe.empty and sort_column in dataframe.columns:
            dataframe = dataframe.sort_values(sort_column)

        parts = math.ceil(len(dataframe) / chunk_size)
        base, _ = os.path.splitext(filename)
        for i in range(parts):
            start = i * chunk_size
            end = start + chunk_size
            chunk = dataframe.iloc[start:end]

            part_filename = f"{base}_part{i+1}.csv"
            chunk.to_csv(
                part_filename,
                index=False,
                encoding="utf-8-sig",
            )
            print(f"Saved {part_filename} ({len(chunk)} rows)")

    def export_liked_tracks(self):
        tracks = self.client.users_likes_tracks().fetch_tracks()

        rows = []
        for track in tracks:
            rows.append({
                ARTIST_COLUMN: ", ".join(a.name for a in track.artists if a.name) if track.artists else "",
                TRACK_COLUMN: track.title,
                ALBUM_COLUMN: track.albums[0].title if track.albums else "",
                TRACK_ID_COLUMN: track.id
            })
        self._save_csv(rows, "likes_tracks.csv", ARTIST_COLUMN)

    def export_disliked_tracks(self):
        tracks = self.client.users_dislikes_tracks().fetch_tracks()

        rows = []
        for track in tracks:
            rows.append({
                ARTIST_COLUMN: ", ".join(a.name for a in track.artists if a.name) if track.artists else "",
                TRACK_COLUMN: track.title,
                ALBUM_COLUMN: track.albums[0].title if track.albums else "",
                TRACK_ID_COLUMN: track.id,
            })
        self._save_csv(rows, "dislikes_tracks.csv", ARTIST_COLUMN)

    def export_liked_albums(self):
        likes = self.client.users_likes_albums()
        rows = []
        for like in likes:
            album = like.album
            if not album:
                continue

            rows.append({
                ARTIST_COLUMN: ", ".join(a.name for a in album.artists if a.name) if album.artists else "",
                ALBUM_COLUMN: album.title,
                ALBUM_ID_COLUMN: album.id,
            })
        self._save_csv(rows, "likes_albums.csv", ARTIST_COLUMN)

    def export_liked_artists(self):
        likes = self.client.users_likes_artists()

        rows = []
        for like in likes:
            if not like.artist:
                continue

            rows.append({
                ARTIST_COLUMN: like.artist.name,
                ARTIST_ID_COLUMN: like.artist.id,
            })
        self._save_csv(rows, "likes_artists.csv", ARTIST_COLUMN)

    def export_all(self) -> None:
        print("Exporting liked tracks...")
        self.export_liked_tracks()

        print("Exporting disliked tracks...")
        self.export_disliked_tracks()

        print("Exporting liked albums...")
        self.export_liked_albums()

        print("Exporting liked artists...")
        self.export_liked_artists()


if __name__ == "__main__":
    yandex_token = get_yandex_token()

    exporter = YandexMusicExporter(token=yandex_token)

    exporter.export_all()
