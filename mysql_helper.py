import mysql.connector
import pandas as pd

def store_incident_data(file_path):
    conn = mysql.connector.connect(
        host='mysql',
        user='root',
        password='password',
        database='incident_event'
    )
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS incidents (
            number VARCHAR(255) PRIMARY KEY,
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
            notify BOOLEAN,
            problem_id VARCHAR(255),
            rfc VARCHAR(255),
            vendor VARCHAR(255),
            caused_by VARCHAR(255),
            closed_code VARCHAR(255),
            resolved_by VARCHAR(255),
            resolved_at DATETIME,
            closed_at DATETIME
        )
    ''')

    # Read the CSV file
    data = pd.read_csv(file_path)
    
    # Insert data into MySQL
    for _, row in data.iterrows():
        cursor.execute('''
            INSERT INTO incidents (
                number, incident_state, active, reassignment_count, reopen_count, sys_mod_count,
                made_sla, caller_id, opened_by, opened_at, sys_created_by, sys_created_at,
                sys_updated_by, sys_updated_at, contact_type, location, category, subcategory,
                u_symptom, cmdb_ci, impact, urgency, priority, assignment_group, assigned_to,
                knowledge, u_priority_confirmation, notify, problem_id, rfc, vendor, caused_by,
                closed_code, resolved_by, resolved_at, closed_at
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        ''', (
            row['number'], row['incident_state'], row['active'], row['reassignment_count'], row['reopen_count'],
            row['sys_mod_count'], row['made_sla'], row['caller_id'], row['opened_by'], row['opened_at'],
            row['sys_created_by'], row['sys_created_at'], row['sys_updated_by'], row['sys_updated_at'],
            row['contact_type'], row['location'], row['category'], row['subcategory'], row['u_symptom'],
            row['cmdb_ci'], row['impact'], row['urgency'], row['priority'], row['assignment_group'],
            row['assigned_to'], row['knowledge'], row['u_priority_confirmation'], row['notify'], row['problem_id'],
            row['rfc'], row['vendor'], row['caused_by'], row['closed_code'], row['resolved_by'],
            row['resolved_at'], row['closed_at']
        ))

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    store_incident_data('incident_event_log.csv')  # Update with your actual CSV file path
