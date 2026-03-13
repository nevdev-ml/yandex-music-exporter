# 🎵 Yandex Music Likes Exporter

---

**Yandex Music Likes Exporter** — это небольшой Python-скрипт для экспорта вашей медиатеки из **Yandex Music**.

Скрипт позволяет выгрузить:

* ❤️ понравившиеся треки
* 👎 дизлайкнутые треки
* 💿 понравившиеся альбомы
* 🎤 понравившихся исполнителей

Все данные сохраняются в **CSV-файлы**, которые удобно анализировать или импортировать на другие ресурсы.

---

## ⚙️ Требования

Перед запуском убедитесь, что установлено:

* 🐍 **Python 3.8+**
* 🌐 **Google Chrome**

---

## ▶️ Запуск через bash-скрипт

Скрипт `run.sh` автоматически:

* создаёт виртуальное окружение `.venv`
* устанавливает зависимости
* запускает экспорт

### Linux / macOS
```bash
chmod +x run.sh
./run.sh
```

### Windows (Git Bash / WSL)

```bash
./run.sh
```

---

## ▶️ Запуск вручную

```bash
python -m venv .venv
```

Linux / macOS

```bash
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Windows (Git Bash)

```bash
source .venv/Scripts/activate
pip install -r requirements.txt
python main.py
```

---

## 📁 Результат

После выполнения появятся файлы:

| Файл                  | Содержимое                |
| --------------------- | ------------------------- |
| `likes_tracks.csv`    | понравившиеся треки       |
| `dislikes_tracks.csv` | дизлайкнутые треки        |
| `likes_albums.csv`    | понравившиеся альбомы     |
| `likes_artists.csv`   | понравившиеся исполнители |

CSV-файлы сохраняются в кодировке **UTF-8 BOM** для корректного открытия в любых редакторах.

---

## 🔐 OAuth токен

При первом запуске откроется браузер для входа в **Yandex**.

После успешной авторизации скрипт автоматически получит **OAuth токен** и сохранит его в `.env`

Можно создать вручную:
```
TOKEN=your_access_token
```

---
**Yandex Music Likes Exporter** is a small Python script that allows you to export your **Yandex Music** library.

The script can export:

* ❤️ liked tracks
* 👎 disliked tracks
* 💿 liked albums
* 🎤 liked artists

All data is saved as **CSV files**, making it easy to analyze or import into other services.

---

## ⚙️ Requirements

Before running the script, make sure you have:

* 🐍 **Python 3.8+**
* 🌐 **Google Chrome**

---

## ▶️ Run with bash script

The `run.sh` script automatically:

* creates a virtual environment `.venv`
* installs dependencies
* runs the exporter

### Linux / macOS

```bash
chmod +x run.sh
./run.sh
```

### Windows (Git Bash / WSL)

```bash
./run.sh
```

---

## ▶️ Run manually

```bash
python -m venv .venv
```

Linux / macOS

```bash
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Windows (Git Bash)

```bash
source .venv/Scripts/activate
pip install -r requirements.txt
python main.py
```

---

## 📁 Output

After running the script, the following files will be generated:

| File                  | Description     |
| --------------------- | --------------- |
| `likes_tracks.csv`    | liked tracks    |
| `dislikes_tracks.csv` | disliked tracks |
| `likes_albums.csv`    | liked albums    |
| `likes_artists.csv`   | liked artists   |

CSV files are saved using **UTF-8 BOM encoding** to ensure they open correctly in most editors.

---

## 🔐 OAuth token

During the first run, a browser window will open for **Yandex authentication**.

After a successful login, the script will automatically obtain an **OAuth token** and save it in `.env`.

You can also create it manually:

```
TOKEN=your_access_token
```
