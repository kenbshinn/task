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
#cursor = conn.cursor()

#Executing a PostgreSQL function using the execute() method
#cursor.execute("SELECT task_name FROM tasks WHERE status_id = 1;")

#Fetching ALL results that match query above. 
#data = cursor.fetchall()
#print("Here are a list of your active tasks: ",data)

print("Welcome to Task. Your home for managing all your tasks in one place.")

menu_options = {
    1: 'Show all Active Tasks',
    2: 'Option 2',
    3: 'Option 3',
    4: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
    cursor = conn.cursor()
    cursor.execute("SELECT task_name FROM tasks WHERE status_id = 1;")
    data = cursor.fetchall()
    print("Here are a list of your active tasks: ",data)
     #print('Handle option \'Option 1\'')

def option2():
     print('Handle option \'Option 2\'')

def option3():
     print('Handle option \'Option 3\'')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')