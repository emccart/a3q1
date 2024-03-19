import psycopg2
from getpass import getpass

dbname = input("Database name?\n")
user = input("user?\n")
password = getpass("password?\n")
host = getpass("host address?\n")
port = input("port?\n")

connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

cur = connection.cursor()

def getAllStudents(cur):
    cur.execute("SELECT * FROM students")
    print(cur.fetchall())
    pass

def addStudent(cur):
    fname = input("First Name?\n")
    lname = input("Last Name?\n")
    email = input("Email?\n")
    enrollment = input("Enrollment Date?\n")
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('"+fname+"', '"+lname+"', '"+email+"', '"+enrollment+"')")
    pass

def updateStudentEmail(cur):
    sid = input("Student ID?\n")
    email = input("Email?\n")
    cur.execute("UPDATE students SET email = '"+email+"' WHERE student_id = "+sid)
    pass

def deleteStudent(cur):
    sid = input("Student ID?\n")
    cur.execute("DELETE FROM students WHERE student_id = " + sid)
    pass

selection = 'c'
while(selection != '5'):
    selection = input(" 1. getAllStudents\n 2. addStudent\n 3. updateStudentEmail\n 4. deleteStudent\n 5. Quit\n")
    if selection == '1':
        getAllStudents(cur)
    elif selection == '2':
        addStudent(cur)
    elif selection == '3':
        updateStudentEmail(cur)
    elif selection == '4':
        deleteStudent(cur)
    elif selection == '5':
        print("Quitting")
    else:
        print("Invalid Selection")


connection.close()

