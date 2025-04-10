# 🧠 Dave AI Log Analyzer

Welcome to **Dave AI Log Analyzer** — a cross-platform Python script that scans `.txt` log files, counts lines and errors, and creates a summary. If you're running in a Linux environment (like Docker), it'll also bundle the logs into a neat `.tar.gz` archive. 💥

Perfect for developers who want a quick overview of what's going on in their logs, especially inside containers or remote environments.

---

## 🚀 Features

- 🔍 Recursively scans directories for `.txt` log files
- 📊 Counts total lines and lines containing the word "error"
- 🆖 Compares Python-based and Unix `wc -l` line counts
- 📆 Archives all log files (in Docker/Linux only)
- 💻 Works on **Windows**, **Linux**, and **Docker**

---

## 🐳 Running in Docker

### 1⃣ Build the Docker image

```bash
docker build -t dave-ai-task .
```

### 2⃣ Run the container with an interactive terminal

```bash
docker run -it dave-ai-task bash
```

### 3⃣ Navigate to the working directory

```bash
cd /app
```

### 4⃣ Run the script

```bash
python script.py
```

👉 When prompted:

```
Enter the full path to the directory (e.g., /home/ubuntu/logs): /app/logs
```

The script will:
- ✅ Generate a `summary.txt` file with log insights
- 📆 Create `logs_archive.tar.gz` (inside the container in pwd)

---

## 📁 Directory Structure

```
dave-ai-log-analyzer/
├── logs/               # Your sample or actual log files
│   ├── log1.txt
│   └── ...
├── script.py           # Main Python script
├── Dockerfile          # For containerized runs
└── README.md           # You're reading this :)
```

---

## 🧪 Example Output

```txt
File: /app/logs/log1.txt
Error Count: 4
Line Count Mismatch: Python=80, wc=82

File: /app/logs/log2.txt
Error Count: 2
```

📝 Summary file: `/app/summary.txt`  
📆 Archive: `/app/logs_archive.tar.gz` (Linux only)

---

## 🧊 Notes

- On **Windows**, the archive feature will be skipped automatically (no native `tar`).
- You can still use all other features including error and line count analysis.
- Make sure paths you provide exist *inside the container* if running via Docker.

---

## 🤊 Author

💻 Made by **Pranav** & ChatGPT 🚀  
---
