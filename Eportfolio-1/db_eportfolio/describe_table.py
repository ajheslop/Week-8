import sqlite3

# Connect to the database
connection = sqlite3.connect("my_database.db")

# Create a cursor
cursor = connection.cursor()

'''PRAGMA table_info: Columns in the result set include the column name,
data type, whether or not the column can be NULL,
and the default value for the column.'''

sql_command = """PRAGMA table_info([students]);"""

# Execute your command
cursor.execute(sql_command)

# Fetch all rows and print
res = cursor.fetchall() 

print(res)