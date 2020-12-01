import sqlite3
import os



# Connect to the database
connection = sqlite3.connect("college_database.db")

# Create a cursor
cursor = connection.cursor()

# Execute your SQL query
cursor.execute("SELECT * FROM students;") 

# Fetch all rows and print
res = cursor.fetchall() 

print("="*50)
print("Basic printing: ")
print("="*50)
print(res)

# Amend to input for Python 3 
input("Press Enter to continue...")



print("="*50)
print("A fancier way of doing it")
print("="*50)

for row in res:
    # row[0] returns the first column in the query (student_number),
    # row[1] returns student_rep name
    print('{0} : {1}. '
            .format(row[0], row[1],))

print("="*50)
print("End of query.")
print("="*50)

