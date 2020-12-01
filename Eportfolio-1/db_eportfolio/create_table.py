import sqlite3

# Connect to the database
connection = sqlite3.connect("college_database.db")

# Create a cursor
cursor = connection.cursor()

# Write your SQL statement
sql_command = """
CREATE TABLE IF NOT EXISTS students ( 
student_number INTEGER PRIMARY KEY, 
student_name VARCHAR(255),
student_age INTEGER(2),
student_grade INTEGER(5)
);

"""

# Execute the statement
cursor.execute(sql_command)

# Commit
connection.commit()








