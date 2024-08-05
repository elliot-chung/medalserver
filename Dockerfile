# https://hub.docker.com/_/python
FROM python:3.10-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ . 

CMD ["fastapi", "run"]