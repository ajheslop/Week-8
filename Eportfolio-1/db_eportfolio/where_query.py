import sqlite3
import os

# Clear output
os.system('clear')

# Connect to the database
connection = sqlite3.connect("college_database.db")

# Create a cursor
cursor = connection.cursor()

# Execute your SQL query
cursor.execute("SELECT * FROM students WHERE student_number = 12122;") 

# Fetch all rows and print
res = cursor.fetchall() 

print("="*50)
print("Basic printing: ")
print("="*50)
print(res)
