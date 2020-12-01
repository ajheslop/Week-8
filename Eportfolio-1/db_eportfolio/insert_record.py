import sqlite3

# Connect to the database
connection = sqlite3.connect("college_database.db")

# Create a cursor
cursor = connection.cursor()

sql_command = """INSERT INTO students (student_number,student_name, student_age, student_grade)
    VALUES (1,"Alan Heslop", 15, 5),
            (2,"Kieran Clayton", 19, 1),
           (3,"Rachael Atkinson", 19, 1);"""

# Execute your command
cursor.execute(sql_command)

# Commit
connection.commit()

