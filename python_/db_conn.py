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

conn = pymysql.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)
cursor = conn.cursor()
cursor.execute("USE practice;")
cursor.execute("select * from employees;")
print(cursor.fetchall())
