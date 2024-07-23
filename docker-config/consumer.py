# import json
# import time
# import mysql.connector
# from kafka import KafkaConsumer
# from pymongo import MongoClient
# from datetime import datetime

# def create_consumer():
#     for _ in range(10):
#         try:
#             consumer = KafkaConsumer(
#                 'Our_topic',
#                 bootstrap_servers='kafka:9092',
#                 auto_offset_reset='earliest',
#                 enable_auto_commit=True,
#                 group_id='my-group',
#                 value_deserializer=lambda x: json.loads(x.decode('utf-8'))
#             )
#             return consumer
#         except Exception as e:
#             print("Kafka server not ready, retrying in 5 seconds...")
#             time.sleep(5)
#     raise Exception("Kafka server not ready after 10 attempts")

# def create_mongo_client():
#     for _ in range(10):
#         try:
#             client = MongoClient('mongo', 27017)
#             return client
#         except Exception as e:
#             print("MongoDB server not ready, retrying in 5 seconds...")
#             time.sleep(5)
#     raise Exception("MongoDB server not ready after 10 attempts")

# def create_mysql_connection():
#     for _ in range(10):
#         try:
#             connection = mysql.connector.connect(
#                 host='mysql',
#                 user='root',
#                 password='password',
#                 database='incident_event'
#             )
#             return connection
#         except Exception as e:
#             print("MySQL server not ready, retrying in 5 seconds...")
#             time.sleep(5)
#     raise Exception("MySQL server not ready after 10 attempts")

# def format_datetime(dt_str):
#     try:
#         # Convert date format to '%Y-%m-%d %H:%M:%S'
#         return datetime.strptime(dt_str, '%d/%m/%Y %H:%M').strftime('%Y-%m-%d %H:%M:%S')
#     except ValueError:
#         return None

# consumer = create_consumer()
# mongo_client = create_mongo_client()
# mysql_connection = create_mysql_connection()
# mysql_cursor = mysql_connection.cursor()

# # Ensure the table structure matches the data schema
# mysql_cursor.execute("""
#     CREATE TABLE IF NOT EXISTS incidents (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         number VARCHAR(255),
#         incident_state VARCHAR(255),
#         active BOOLEAN,
#         reassignment_count INT,
#         reopen_count INT,
#         sys_mod_count INT,
#         made_sla BOOLEAN,
#         caller_id VARCHAR(255),
#         opened_by VARCHAR(255),
#         opened_at DATETIME,
#         sys_created_by VARCHAR(255),
#         sys_created_at DATETIME,
#         sys_updated_by VARCHAR(255),
#         sys_updated_at DATETIME,
#         contact_type VARCHAR(255),
#         location VARCHAR(255),
#         category VARCHAR(255),
#         subcategory VARCHAR(255),
#         u_symptom VARCHAR(255),
#         cmdb_ci VARCHAR(255),
#         impact VARCHAR(255),
#         urgency VARCHAR(255),
#         priority VARCHAR(255),
#         assignment_group VARCHAR(255),
#         assigned_to VARCHAR(255),
#         knowledge BOOLEAN,
#         u_priority_confirmation BOOLEAN,
#         notify VARCHAR(255),
#         problem_id VARCHAR(255),
#         rfc VARCHAR(255),
#         vendor VARCHAR(255),
#         caused_by VARCHAR(255),
#         closed_code VARCHAR(255),
#         resolved_by VARCHAR(255),
#         resolved_at DATETIME,
#         closed_at DATETIME
#     )
# """)

# db = mongo_client.incident_event
# collection = db.incidents

# for message in consumer:
#     data = message.value
#     collection.insert_one(data)
#     print(f"Data to insert: {data}")  # Debug print statement

#     try:
#         query = """
#             INSERT INTO incidents (
#                 number, 
#                 incident_state, 
#                 active, 
#                 reassignment_count, 
#                 reopen_count, 
#                 sys_mod_count,
#                 made_sla, 
#                 caller_id, 
#                 opened_by, 
#                 opened_at, 
#                 sys_created_by, 
#                 sys_created_at,
#                 sys_updated_by, 
#                 sys_updated_at, 
#                 contact_type, 
#                 location, 
#                 category, 
#                 subcategory,
#                 u_symptom, 
#                 cmdb_ci, 
#                 impact, 
#                 urgency, 
#                 priority, 
#                 assignment_group, 
#                 assigned_to,
#                 knowledge, 
#                 u_priority_confirmation, 
#                 notify, 
#                 problem_id, 
#                 rfc, 
#                 vendor, 
#                 caused_by,
#                 closed_code, 
#                 resolved_by, 
#                 resolved_at, 
#                 closed_at
#             ) VALUES (
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s, 
#                 %s,
#                 %s,
#                 %s
#             )
#         """
#         params = (
#             data['number'], data['incident_state'], int(data['active']),
#             int(data['reassignment_count']), int(data['reopen_count']),
#             int(data['sys_mod_count']), int(data['made_sla']),
#             data['caller_id'], data['opened_by'], format_datetime(data['opened_at']),
#             data['sys_created_by'], format_datetime(data['sys_created_at']),
#             data['sys_updated_by'], format_datetime(data['sys_updated_at']),
#             data['contact_type'], data['location'], data['category'],
#             data['subcategory'], data['u_symptom'], data['cmdb_ci'],
#             data['impact'], data['urgency'], data['priority'],
#             data['assignment_group'], data['assigned_to'],
#             int(data['knowledge']), int(data['u_priority_confirmation']),
#             data['notify'], data['problem_id'], data['rfc'], data['vendor'],
#             data['caused_by'], data['closed_code'], data['resolved_by'],
#             format_datetime(data['resolved_at']), format_datetime(data['closed_at'])
#         )

#         # Debug output
#         print(f"SQL Query: {query}")
#         print(f"Parameters: {params}")

#         mysql_cursor.execute(query, params)
#         mysql_connection.commit()
#         print(f"Inserted into MySQL: {data}")  # Debug print statement
#     except mysql.connector.Error as e:
#         print(f"Error inserting into MySQL: {e}")

# mysql_cursor.close()
# mysql_connection.close()


import json
import time
import mysql.connector
from kafka import KafkaConsumer
from pymongo import MongoClient
from datetime import datetime

def create_kafka_consumer():
    """Create and return a KafkaConsumer with retries."""
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

def create_mongo_client():
    """Create and return a MongoClient with retries."""
    for _ in range(10):
        try:
            return MongoClient('mongo', 27017)
        except Exception as e:
            print("MongoDB server not ready, retrying in 5 seconds...")
            time.sleep(5)
    raise Exception("MongoDB server not ready after 10 attempts")

def create_mysql_connection():
    """Create and return a MySQL connection with retries."""
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
    """Format date string to '%Y-%m-%d %H:%M:%S'."""
    try:
        return datetime.strptime(dt_str, '%d/%m/%Y %H:%M').strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        return None

# Initialize Kafka consumer, MongoDB client, and MySQL connection
consumer = create_kafka_consumer()
mongo_client = create_mongo_client()
mysql_connection = create_mysql_connection()
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
