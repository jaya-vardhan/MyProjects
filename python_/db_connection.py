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

# def create_tables(cursor, connection):
#     cursor.execute(
#         """
#         CREATE TABLE employees (
#             employee_id INT PRIMARY KEY AUTO_INCREMENT,
#             first_name VARCHAR(50) NOT NULL,
#             last_name VARCHAR(50) NOT NULL,
#             department VARCHAR(50)
#         );
#         """
#     )
#     cursor.execute(
#         """
#         INSERT INTO employees (first_name, last_name, department)
#         VALUES
#             ('Jane', 'Smith', 'Sales'),
#             ('Peter', 'Jones', 'Engineering'),
#             ('Susan', 'Miller', 'Marketing');
#         """
#     )
#     connection.commit()


# def fetch_data(cursor):
#     cursor.execute("select * from employees;")
#     for data in cursor.fetchall():
#         time.sleep(10)
#         print(data)

# def test_cpu(connection, cursor):
#     print("test_cpu")
#     print("Running CPU-heavy query...")
#     start = time.time()

#     cursor.execute("SELECT BENCHMARK(5000000000000, MD5('test'));")

#     print(cursor.fetchall())

#     print("Done in", time.time() - start, "seconds")


# try:
#     # Create connection
    # connection = pymysql.connect(
    #     host=host,
    #     port=port,
    #     user=user,
    #     password=password,
    #     database=database
    # )
#     print("✅ Connected to MySQL RDS")

#     # Create cursor
#     cursor = connection.cursor()

#     # Run a query
#     # cursor.execute("SHOW DATABASES;")
#     # cursor.execute("create database practice;")
#     cursor.execute("USE practice;")
#     # create_tables(cursor, connection)

#     # fetch_data(cursor)
#     test_cpu(connection, cursor)

# except pymysql.MySQLError as e:
#     print(f"❌ Error: {e}")

import pymysql
import threading

def cpu_task():
    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    cursor = conn.cursor()
    print("Thread started")
    cursor.execute("SELECT BENCHMARK(5000000000000, SHA1('abc'));")
    # cursor.close()
    # conn.close()
    print("Thread done")

threads = []

NUM_THREADS = 40

for i in range(NUM_THREADS):
    t = threading.Thread(target=cpu_task)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads finished")
