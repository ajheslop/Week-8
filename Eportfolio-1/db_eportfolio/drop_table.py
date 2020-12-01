import sqlite3

# Connect to the database
connection = sqlite3.connect("college_database.db")

# Create a cursor
cursor = connection.cursor()

# Drop the table
cursor.execute("DELETE FROM students WHERE student_number = 67832")

# Commit
connection.commit()
