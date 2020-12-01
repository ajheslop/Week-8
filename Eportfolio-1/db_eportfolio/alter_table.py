import sqlite3


# Connect to the database
connection = sqlite3.connect("college_database.db")

# Create a cursor
cursor = connection.cursor()

cursor.execute("""ALTER TABLE students ADD COLUMN
    student_second_name VARCHAR(30);""")