#Importing SQLite3 Library
import sqlite3 as sql

#creating database
db = sql.connect('database_python_programming.db')

#Create a table called python_programming
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE python_programming(id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)
''')

db.commit()

#Insert the following new rows into the python_programming table:
#creating id, name and grade
id1 = 55
name1 = 'Clark Davis'
grade1 = 61

id2 = 66
name2 = 'Dennis Fredrickson'
grade2 = 88

id3 = 77
name3 = 'Jane Richards'
grade3 = 78

id4 = 12
name4 = 'Peyton Sawyer'
grade4 = 45

id5 = 2
name5 = 'Lucas Brooke'
grade5 = 99

#creating list of id, name and grade
students = [(id1,name1, grade1),(id2,name2, grade2),(id3,name3, grade3),(id4,name4, grade4),(id5,name5, grade5)]

#insert several user, use executemany and a list with the tuples.
cursor.executemany('''INSERT INTO python_programming(id, name,grade) VALUES(?,?,?)''', students)
db.commit()

cursor.execute('''SELECT id, name, grade FROM python_programming''')
print('Printing Tables from database')
result = cursor.fetchall()
for row in result:
    print(row)

#Select all records with a grade between 60 and 80
print()
print('Select all records with a grade between 60 and 80')
query = 'SELECT id, name, grade FROM python_programming WHERE grade BETWEEN 60 AND 80'
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)

#Change Carl Davis’s grade to 65
print()    
print('Change Carl Davis’s grade to 65.')
query = "UPDATE python_programming SET grade = 65 WHERE name = 'Clark Davis'"
cursor.execute(query)
db.commit()

query = "SELECT id, name, grade FROM python_programming WHERE name = 'Clark Davis'"
cursor.execute(query)
result = cursor.fetchone()
print(result)

#Delete Dennis Fredrickson’s row.
print()
print('Delete Dennis Fredrickson’s row.')
query = "DELETE FROM python_programming WHERE name = 'Dennis Fredrickson'"
cursor.execute(query)
db.commit()
cursor.execute('''SELECT id, name, grade FROM python_programming''')
result = cursor.fetchall()
for row in result:
    print(row)
    
#Change the grade of all people with an id below than 55
print()
print('Change the grade of all people with an id below than 55')
query = "UPDATE python_programming SET grade = 50 WHERE id < 55"
cursor.execute(query)
db.commit()
cursor.execute('''SELECT id, name, grade FROM python_programming''')
result = cursor.fetchall()
for row in result:
    print(row)