import pandas as pd
from kafka import KafkaProducer
import json
import time

def create_producer():
    for _ in range(10):  # Retry 10 times
        try:
            producer = KafkaProducer(
                bootstrap_servers='kafka:9092',
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            return producer
        except Exception as e:
            print("Kafka server not ready, retrying in 5 seconds...")
            time.sleep(5)
    raise Exception("Kafka server not ready after 10 attempts")

def read_data():
    df = pd.read_csv('incident_event_log.csv')
    return df.to_dict(orient='records')

producer = create_producer()
data = read_data()

for record in data:
    producer.send('Our_topic', value=record)
    print(f'Sent: {record}')
    time.sleep(0.1)  # Adjust the sleep time as needed

producer.flush()
