# 🗂️ Log Archive CLI Tool

A simple Python CLI tool to archive logs by compressing them into timestamped `.tar.gz` files and storing them in a separate directory. This is helpful for keeping your system clean, organized, and maintaining older logs in a compressed format for future reference.

---

## 🚀 Features

- ✅ Archive logs from any specified directory
- ✅ Create compressed `.tar.gz` archives
- ✅ Automatically name archives with current date and time
- ✅ Store archives in a separate `archived_logs/` directory
- ✅ Log each archive operation in a `archive_log.txt` file

---

## 📦 Requirements

- Python 3.6+

---

## 🔧 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/log-archive-cli.git
cd log-archive-cli
```

## Usage
Make it executable:
```
chmod +x log_archive.py
python3 log_archive.py /var/log
```

## Output
Compressed archive: archived_logs/logs_archive_YYYYMMDD_HHMMSS.tar.gz
Log file: archived_logs/archive_log.txt

## Schedule Archiving (Optional)
To automate the archiving process using cron:
```
crontab -e
```

## Project
[https://roadmap.sh/projects/log-archive-tool]
