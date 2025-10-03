import pymysql
import os
from dotenv import load_dotenv
import time

load_dotenv()

# Replace with your RDS connection details
host = os.getenv('DB_HOST')
port = int(os.getenv('DB_PORT'))
user = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
database = os.getenv('DB_NAME')

try:
    # Create connection
    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    print("✅ Connected to MySQL RDS")

    # Create cursor
    cursor = connection.cursor()

    # Run a query
    # cursor.execute("SHOW DATABASES;")
    cursor.execute("USE practice;")
    # cursor.execute("show tables;")
    # cursor.execute(
    #     """
    #     CREATE TABLE employees (
    #         employee_id INT PRIMARY KEY AUTO_INCREMENT,
    #         first_name VARCHAR(50) NOT NULL,
    #         last_name VARCHAR(50) NOT NULL,
    #         department VARCHAR(50)
    #     );
    #     """
    # )
    # cursor.execute(
    #     """
    #     INSERT INTO employees (first_name, last_name, department)
    #     VALUES
    #         ('Jane', 'Smith', 'Sales'),
    #         ('Peter', 'Jones', 'Engineering'),
    #         ('Susan', 'Miller', 'Marketing');
    #     """
    # )
    # cursor.execute("select * from employees;")
    # # connection.commit()

    # # Fetch results
    # for db in cursor.fetchall():
    #     time.sleep(10)
    #     print(db)

    while True:
        cursor.execute("select * from employees;")
        for db in cursor.fetchall():
            time.sleep(5)
            print(db)

except pymysql.MySQLError as e:
    print(f"❌ Error: {e}")
