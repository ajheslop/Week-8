import sqlite3

# Connect to the database
connection = sqlite3.connect("college_database.db")

# Create a cursor
cursor = connection.cursor()

# Write your SQL query
sql_command = """SELECT students.student_number, student_rep, role, department
                 FROM students 
                 JOIN student_rep ON students.student_rep = student_rep.name
                 WHERE students.student_number IN (23682,33289)"""

# Execute your command
cursor.execute(sql_command)

# Fetch all rows and print
res = cursor.fetchall() 

print("="*50)
print("Student Numbers and there Student Rep details:")
print("="*50)

for row in res:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('Student Number: {0} || Student Rep: {1} || Role: {2} || Department: {3}'
            .format(row[0], row[1], row[2], row[3]))

