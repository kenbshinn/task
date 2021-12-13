import psycopg2
import os

DB_SERVER = os.environ.get('DB_SERVER')
DATABASE = os.environ.get('DATABASE')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_PORT = os.environ.get('DB_PORT')


#Establish Database Connnection
#conn = psycopg2.connect(
    #database=DATABASE, user=DB_USER, password=DB_PASS, host=DB_SERVER, port=DB_PORT
#) 

def get_tasks():
    """ query tasks from the tasks table """
    conn = None
    try:
        #params = config(database=DATABASE, user=DB_USER, password=DB_PASS, host=DB_SERVER, port=DB_PORT)
        conn = psycopg2.connect(database=DATABASE, user=DB_USER, password=DB_PASS, host=DB_SERVER, port=DB_PORT)
        cur = conn.cursor()
        cur.execute("SELECT task_id FROM tasks ORDER BY task_id")
        rows = cur.fetchall()
        print("The number of tasks: ", cur.rowcount)
        for row in rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    get_tasks()