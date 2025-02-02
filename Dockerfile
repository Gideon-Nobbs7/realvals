FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONDONUNBUFFERED 1

WORKDIR /app

COPY  requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod 666 db.sqlite3

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
