FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    findutils \
    coreutils \
    tar \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY logs ./logs

COPY script.py .

CMD ["python", "script.py"]
