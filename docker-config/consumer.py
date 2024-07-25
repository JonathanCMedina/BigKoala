"""
Kafka to MongoDB and MySQL Data Pipeline

This script sets up a Kafka consumer to ingest data from a Kafka topic, stores the data in MongoDB,
and then transfers it to a MySQL database.

Dependencies:
- json
- time
- mysql.connector
- kafka
- pymongo
- datetime

Functions:
- kafka_consumer: Initializes and returns a KafkaConsumer instance.
- mongo_consumer: Initializes and returns a MongoClient instance.
- mysql_consumer: Initializes and returns a MySQL connection.
- format_datetime: Formats a date string to '%Y-%m-%d %H:%M:%S'.

Main Workflow:
1. Initialize Kafka consumer, MongoDB client, and MySQL connection.
2. Create a table in MySQL if it doesn't exist.
3. Consume messages from Kafka.
4. Insert data into MongoDB.
5. Transfer data from MongoDB to MySQL.

"""

import json
import time
import mysql.connector
from kafka import KafkaConsumer
from pymongo import MongoClient
from datetime import datetime

def kafka_consumer():
    """
    Create and return a KafkaConsumer with retries.

    Returns:
        KafkaConsumer: An instance of KafkaConsumer.
    
    Raises:
        Exception: If Kafka server is not ready after 10 attempts.
    """
    for _ in range(10):
        try:
            return KafkaConsumer(
                'Our_topic',
                bootstrap_servers='kafka:9092',
                auto_offset_reset='earliest',
                enable_auto_commit=True,
                group_id='my-group',
                value_deserializer=lambda x: json.loads(x.decode('utf-8'))
            )
        except Exception as e:
            print("Kafka server not ready, retrying in 5 seconds...")
            time.sleep(5)
    raise Exception("Kafka server not ready after 10 attempts")

def mongo_consumer():
    """
    Create and return a MongoClient with retries.

    Returns:
        MongoClient: An instance of MongoClient.
    
    Raises:
        Exception: If MongoDB server is not ready after 10 attempts.
    """
    for _ in range(10):
        try:
            return MongoClient('mongo', 27017)
        except Exception as e:
            print("MongoDB server not ready, retrying in 5 seconds...")
            time.sleep(5)
    raise Exception("MongoDB server not ready after 10 attempts")

def mysql_consumer():
    """
    Create and return a MySQL connection with retries.

    Returns:
        MySQLConnection: An instance of MySQLConnection.
    
    Raises:
        Exception: If MySQL server is not ready after 10 attempts.
    """
    for _ in range(10):
        try:
            return mysql.connector.connect(
                host='mysql',
                user='root',
                password='password',
                database='incident_event'
            )
        except Exception as e:
            print("MySQL server not ready, retrying in 5 seconds...")
            time.sleep(5)
    raise Exception("MySQL server not ready after 10 attempts")

def format_datetime(dt_str):
    """
    Format date string to '%Y-%m-%d %H:%M:%S'.

    Args:
        dt_str (str): Date string in the format '%d/%m/%Y %H:%M'.

    Returns:
        str: Formatted date string or None if the input format is incorrect.
    """
    try:
        return datetime.strptime(dt_str, '%d/%m/%Y %H:%M').strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        return None

# Initialize Kafka consumer, MongoDB client, and MySQL connection
consumer = kafka_consumer()
mongo_client = mongo_consumer()
mysql_connection = mysql_consumer()
mysql_cursor = mysql_connection.cursor()

# Ensure the table structure matches the data schema
mysql_cursor.execute("""
    CREATE TABLE IF NOT EXISTS incidents (
        id INT AUTO_INCREMENT PRIMARY KEY,
        number VARCHAR(255),
        incident_state VARCHAR(255),
        active BOOLEAN,
        reassignment_count INT,
        reopen_count INT,
        sys_mod_count INT,
        made_sla BOOLEAN,
        caller_id VARCHAR(255),
        opened_by VARCHAR(255),
        opened_at DATETIME,
        sys_created_by VARCHAR(255),
        sys_created_at DATETIME,
        sys_updated_by VARCHAR(255),
        sys_updated_at DATETIME,
        contact_type VARCHAR(255),
        location VARCHAR(255),
        category VARCHAR(255),
        subcategory VARCHAR(255),
        u_symptom VARCHAR(255),
        cmdb_ci VARCHAR(255),
        impact VARCHAR(255),
        urgency VARCHAR(255),
        priority VARCHAR(255),
        assignment_group VARCHAR(255),
        assigned_to VARCHAR(255),
        knowledge BOOLEAN,
        u_priority_confirmation BOOLEAN,
        notify VARCHAR(255),
        problem_id VARCHAR(255),
        rfc VARCHAR(255),
        vendor VARCHAR(255),
        caused_by VARCHAR(255),
        closed_code VARCHAR(255),
        resolved_by VARCHAR(255),
        resolved_at DATETIME,
        closed_at DATETIME
    )
""")

db = mongo_client.incident_event
collection = db.incidents

# Main loop to process messages from Kafka
for message in consumer:
    data = message.value
    collection.insert_one(data)
    print(f"Data to insert: {data}")  # Debug print statement

    try:
        query = """
            INSERT INTO incidents (
                number, incident_state, active, reassignment_count, reopen_count, sys_mod_count,
                made_sla, caller_id, opened_by, opened_at, sys_created_by, sys_created_at,
                sys_updated_by, sys_updated_at, contact_type, location, category, subcategory,
                u_symptom, cmdb_ci, impact, urgency, priority, assignment_group, assigned_to,
                knowledge, u_priority_confirmation, notify, problem_id, rfc, vendor, caused_by,
                closed_code, resolved_by, resolved_at, closed_at
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        """
        params = (
            data.get('number'), data.get('incident_state'), int(data.get('active', 0)),
            int(data.get('reassignment_count', 0)), int(data.get('reopen_count', 0)),
            int(data.get('sys_mod_count', 0)), int(data.get('made_sla', 0)),
            data.get('caller_id'), data.get('opened_by'), format_datetime(data.get('opened_at')),
            data.get('sys_created_by'), format_datetime(data.get('sys_created_at')),
            data.get('sys_updated_by'), format_datetime(data.get('sys_updated_at')),
            data.get('contact_type'), data.get('location'), data.get('category'),
            data.get('subcategory'), data.get('u_symptom'), data.get('cmdb_ci'),
            data.get('impact'), data.get('urgency'), data.get('priority'),
            data.get('assignment_group'), data.get('assigned_to'),
            int(data.get('knowledge', 0)), int(data.get('u_priority_confirmation', 0)),
            data.get('notify'), data.get('problem_id'), data.get('rfc'), data.get('vendor'),
            data.get('caused_by'), data.get('closed_code'), data.get('resolved_by'),
            format_datetime(data.get('resolved_at')), format_datetime(data.get('closed_at'))
        )

        # Debug output
        print(f"SQL Query: {query}")
        print(f"Parameters: {params}")

        mysql_cursor.execute(query, params)
        mysql_connection.commit()
        print(f"Inserted into MySQL: {data}")  # Debug print statement
    except mysql.connector.Error as e:
        print(f"Error inserting into MySQL: {e}")

# Cleanup
mysql_cursor.close()
mysql_connection.close()
