"""
Kafka Log Producer

This script reads incident event data from a CSV file and sends it to a Kafka topic.

Dependencies:
- pandas
- kafka-python
- json
- time

Functions:
- create_producer: Initializes and returns a KafkaProducer instance.
- read_data: Reads incident event data from a CSV file and returns it as a list of dictionaries.

Main Workflow:
1. Initialize Kafka producer.
2. Read data from CSV file.
3. Send each record to the Kafka topic.
4. Flush the producer to ensure all messages are sent.

"""

import pandas as pd
from kafka import KafkaProducer
import json
import time

def create_producer():
    """
    Create and return a KafkaProducer with retries.

    Returns:
        KafkaProducer: An instance of KafkaProducer.
    
    Raises:
        Exception: If Kafka server is not ready after 10 attempts.
    """
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
    """
    Read data from the CSV file.

    Returns:
        list: A list of dictionaries where each dictionary represents a record from the CSV file.
    """
    df = pd.read_csv('incident_event_log.csv')
    return df.to_dict(orient='records')

# Initialize Kafka producer
producer = create_producer()

# Read data from CSV file
data = read_data()

# Send each record to the Kafka topic
for record in data:
    producer.send('Our_topic', value=record)
    print(f'Sent: {record}')
    time.sleep(0.1)  # Adjust the sleep time as needed

# Ensure all messages are sent
producer.flush()
