import sqlite3

# Connect to the database
connection = sqlite3.connect("college_database.db")

# Create a cursor
cursor = connection.cursor()

# Delete the record
cursor.execute("DELETE from students")

# Commit changes
connection.commit()
