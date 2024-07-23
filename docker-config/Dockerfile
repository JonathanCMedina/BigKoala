FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY produce_logs.py .
COPY consumer.py .
COPY incident_event_log.csv .

CMD ["python", "kafka_producer.py"]
