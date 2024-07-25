FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY producer.py .
COPY consumer.py .
COPY incident_event_log.csv .

CMD ["python"]
