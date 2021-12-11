import psycopg2
import os

DB_SERVER = os.environ.get('DB_SERVER')
DATABASE = os.environ.get('DATABASE')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_PORT = os.environ.get('DB_PORT')


#Establish Database Connnection
conn = psycopg2.connect(
    database=DATABASE, user=DB_USER, password=DB_PASS, host=DB_SERVER, port=DB_PORT
)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing a PostgreSQL function using the execute() method
cursor.execute("SELECT task_name FROM tasks WHERE status_id = 1;")

#Fetching ALL results that match query above. 
data = cursor.fetchall()
print("Here are a list of your active tasks: ",data)
