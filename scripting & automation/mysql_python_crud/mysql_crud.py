# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 10:42:57 2020

@author: simiyu
"""

from mysql.connector import connect
import pandas.io.sql as sql


db_name = "sample_db"
table_name ="emplyee"
db_user = "root"
db_user_pass = ""


def is_mysql_connection_available(connection):
    print('Attempting to connect to the database...')
    if connection.is_connected():
        print("Connection to the database established successfully")
        return True
    else:
        print("No Connection to the database !!!")
        return False


def display_all_emplyee(connection, table_name):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM "+str(table_name)+";")
    records = cursor.fetchall()

    heading = f"Total registered "+str(table_name)+"s in the system: {cursor.rowcount}"
    print(heading)
    print ("-" * len(heading))
    for row in records:
        print(f"Name: {row[0]}")
        print(f"Age: {row[1]}\n")

    cursor.close()
    connection.close()
    print("MySQL connection is closed")

def export_to_excel(connection, table_name):
    # read the data
    df = sql.read_sql("select * from "+str(table_name)+";", connection)
    # export the data into the excel sheet
    df.to_excel('employees.xlsx')
    print("Employees exported to employees.xlsx")


def add_new_emplyee(connection, table_name,emplyee):
    sql_stmt = """INSERT INTO """+str(table_name)+""" (name,age) VALUES (%s,%s)"""

    cursor = connection.cursor(prepared=True)
    cursor.execute(sql_stmt,emplyee)
    connection.commit()
    cursor.close()
    connection.close()

    print("Record successfully inserted into the database using prepared stament")


def search_emplyee(connection, table_name,query):
    sql_stmt = f"SELECT * FROM "+str(table_name)+" WHERE name LIKE '%{query}%'"

    cursor = connection.cursor()
    cursor.execute(sql_stmt)
    records = cursor.fetchall()

    heading = f"search for '{query}' returned: {cursor.rowcount} rows"
    print(heading)
    print ("-" * len(heading))
    for row in records:
        print(f"Name: {row[0]}")
        print(f"Age: {row[1]}\n")

    cursor.close()
    connection.close()
    print("MySQL connection is closed")


def update_emplyee(connection, table_name, emplyee):
    sql_stmt = "UPDATE "+str(table_name)+" SET name = %s,age = %s WHERE id = %s"

    cursor = connection.cursor(prepared=True)
    cursor.execute(sql_stmt,emplyee)
    connection.commit()
    cursor.close()
    connection.close()

    print("Record successfully updated in the database using prepared stament")

def delete_emplyee(connection, table_name,id):
    sql_stmt = "DELETE FROM "+str(table_name)+" WHERE id = "+str(id)
    cursor = connection.cursor(prepared=True)
    cursor.execute(sql_stmt)
    connection.commit()
    cursor.close()
    connection.close()

    print("Record successfully deleted from the database using prepared stament")



def main():
    print("**** Follow the prompts carefully ****")


    mydb = connect(host="localhost",  user=db_user,  passwd=db_user_pass)

    if is_mysql_connection_available(mydb):
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS "+str(db_name))

        mydbtable = connect(host="localhost",  user=db_user,  passwd=db_user_pass, database=db_name)
        if is_mysql_connection_available(mydbtable):
            mycursortb = mydbtable.cursor()
            mycursortb.execute("CREATE TABLE IF NOT EXISTS "+str(table_name)+" (name VARCHAR(255), age INT,id INT NOT NULL AUTO_INCREMENT, PRIMARY KEY (id))")

            choice = str(input("Enter 'C' to add, 'R' to view single,'L' to list, 'E' to export to excel 'U' to update 'D' to delete and 'Q' to quit  : "))
            if(choice == 'C'):
                name = str(input("Enter Employee Full Name  : "))
                age = int(input("Enter Employee Age  : "))
                employee = (name, age)
                add_new_emplyee(mydbtable, table_name,employee)
                main()

            elif(choice == 'R'):
                name = str(input("Enter Employee Name or a part of name  : "))
                search_emplyee(mydbtable, table_name,name)
                main()

            elif(choice == 'L'):
                display_all_emplyee(mydbtable, table_name)
                main()

            elif(choice == 'E'):
                export_to_excel(mydbtable, table_name)
                main()
            elif(choice == 'U'):
                emplid = int(input("Enter Employee Id  : "))
                name = str(input("Enter Updated Employee Full Name  : "))
                age = int(input("Enter Updated Employee Age  : "))
                employee = (name, age, emplid)
                update_emplyee(mydbtable, table_name,employee)
                main()

            elif(choice == 'D'):
                emplid = int(input("Enter Employee Id  : "))
                delete_emplyee(mydbtable, table_name,emplid)
                main()

            elif (choice == 'Q'):
                raise SystemExit

            else:
                main()
        else:
            print("**** Please Provide valid database connection ****")
    else:
        print("**** Please Provide valid database connection ****")



if __name__ == '__main__':
    main()