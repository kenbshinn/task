import os

DB_SERVER = os.environ.get('DB_SERVER')
DATABASE = os.environ.get('DATABASE')
db_user = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_PORT = os.environ.get('DB_PORT')

print(db_user)
print(DB_SERVER)