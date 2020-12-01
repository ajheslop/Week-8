import sqlite3

''' Script to create the database "college_database"
    and its associated tables: "students", "student_rep" and 
    "class_enrolments" then insert records into those tables'''

print("="*100)
print("Start of script")
print("="*100)

# Connect to the database
connection = sqlite3.connect("college_database.db")

# Create a cursor
cursor = connection.cursor()

print("="*100)
print("DATABASE CREATED: college_database.db")
print("="*100)


# Create the "students" table
sql_command = """
CREATE TABLE IF NOT EXISTS students  ( 
student_number INTEGER PRIMARY KEY, 
student_name VARCHAR(255))
"""

# Execute the statement
cursor.execute(sql_command)

print("="*100)
print("TABLE CREATED: students")
print("="*100)

# Create the "student_rep" table
sql_command = """
CREATE TABLE IF NOT EXISTS student_rep( 
name VARCHAR(30), 
role VARCHAR(30),
department VARCHAR(30))
"""

# Execute the statement
cursor.execute(sql_command)

print("="*100)
print("TABLE CREATED: student_rep")
print("="*100)

# Create the "class_enrolments" table
sql_command = """
CREATE TABLE IF NOT EXISTS class_enrolments( 
student_number INTEGER, 
class_number INTEGER)
"""

# Execute the statement
cursor.execute(sql_command)

print("="*100)
print("TABLE CREATED: class_enrolments")
print("="*100)

print("="*100)
print("INSERTING RECORDS...")
print("="*100)

# INSERT records into "students" table
sql_command = """INSERT INTO students (student_number,student_name)
    VALUES (23682,"Brian Jones"),
           (33289,"Susan Smith");"""

# Execute your command
cursor.execute(sql_command)

# Commit
connection.commit()

# INSERT records into "student_rep" table
sql_command = """INSERT INTO student_rep (name,role,department)
    VALUES ("Brian Jones","Lecturer","Computing"),
           ("Susan Smith", "Senior Lecturer","Science");"""

# Execute your command
cursor.execute(sql_command)

# Commit
connection.commit()

# INSERT records into "class_enrolments" table
sql_command = """INSERT INTO class_enrolments (student_number,class_number)
    VALUES (23682,	1001),
           (23682,	1004),
           (23682,	2202),
           (33289,	3123),
           (33289,	2001),
           (33289,	3001);"""

# Execute your command
cursor.execute(sql_command)

# Commit
connection.commit()


# Select everything from "students" table
cursor.execute("SELECT * FROM students") 

# Get all records returned
res = cursor.fetchall() 

print("="*100)
print("Everything in the 'students' table: ")
print("="*100)

for row in res:
    ''' row[0] returns the first column in the query (student_number),
        row[1] returns student_rep. '''

    print('Student Number: {0} || Student Rep: {1}'
            .format(row[0], row[1]))


# Select everything from "students" table
cursor.execute("SELECT * FROM student_rep") 

# Get all records returned
res = cursor.fetchall() 

print("="*100)
print("Everything in the 'student_rep' table: ")
print("="*100)

for row in res:
    ''' row[0] returns the first column in the query (name),
        row[1] returns role
        row[2] returns department '''

    print('Name: {0} || Role: {1} || Department: {2}'
            .format(row[0], row[1], row[2]))

# Select everything from "class_enrolments" table
cursor.execute("SELECT * FROM class_enrolments") 

# Get all records returned
res = cursor.fetchall() 

print("="*100)
print("Everything in the 'class_enrolments' table: ")
print("="*100)

for row in res:
    ''' row[0] returns the first column in the query (student_number),
        row[1] returns class_number '''

    print('Student Number: {0} || Class Number: {1}'
            .format(row[0], row[1]))

print("="*100)
print("End of script")
print("="*100)


