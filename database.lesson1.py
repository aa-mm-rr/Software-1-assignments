import mysql.connector
'''
def get_employees_by_last_name(last_name):
    sql = f'select lastname, firstname, salary from Employee1 where LastName="{last_name}"'
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0:
        for row in result:
            print(f'Hello! im {row[0]} {row[1]}. My salary is {row[2]} euros per month')
    return

connection=mysql.connector.connect(
    user='myuserl',
    password='mypassword',
    host='127.0.0.1',
    port=3306,
    database ='maridb',
    charset='utf8mb4',
    collation='utf8mb4_general_ci'
)


def get_employees_by_last_name(last_name):
    sql = 'SELECT lastname, firstname, salary FROM Employee1 WHERE LastName = %s'
    cursor = connection.cursor()
    cursor.execute(sql, (last_name,))
    result = cursor.fetchall()
    cursor.close()

    if result:
        for row in result:
            print(f'Hello! I\'m {row[1]} {row[0]}. My salary is {row[2]} euros per month')
    else:
        print('No employees found with that last name.')

    return result
last_name = input('Enter last name: ')
get_employees_by_last_name(last_name)
'''
def update_salary(lastName, new_salary):
   connection = mysql.connector.connect(
       user='myuserl',
       password='password',
       host='127.0.0.1',
       port=3306,
       database='maridb',
       charset='utf8mb4',
       collation='utf8mb4_general_ci'
   )
   cursor = connection.cursor()
   sql = 'update employee1 set salary = %s where number = %s'
   cursor.execute(sql, (new_salary, number))
   if cursor.rowcount == 1:
       print('salary updated successfully')
   else:
       print('Something went wrong')

number = int(input('Enter number: '))
new_salary = float(input('Enter new salary: '))
update_salary(number, new_salary)