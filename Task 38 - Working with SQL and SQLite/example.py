import sqlite3
db = sqlite3.connect('data/student_db')
cursor = db.cursor()  # Get a cursor object

cursor.execute('''
    CREATE TABLE student(id INTEGER PRIMARY KEY, name TEXT,
                   	grade INTEGER)
''')
db.commit()

cursor = db.cursor()
name1 = 'Andres'
grade1 = 60


name2 = 'John'
grade2 = 90

# Insert student 1
cursor.execute('''INSERT INTO student(name, grade)
                  VALUES(?,?)''', (name1, grade1))
print('First user inserted')

# Insert student 2
cursor.execute('''INSERT INTO student(name, grade)
                  VALUES(?,?)''', (name2, grade2))
print('Second user inserted')

db.commit()

id = cursor.lastrowid
print('Last row id: %d' % id)

id = 1
cursor.execute('''SELECT name, grade FROM student  WHERE id=?''', (id,))
student = cursor.fetchone()
print('Data retrieved about student with id %d:' % id)
print(student)

grade = 100
id = 1
cursor.execute('''UPDATE student SET grade = ? WHERE id = ? ''', (grade, id))
print('Student data updated!')


print('SELECT name, grade FROM student:')
cursor.execute('''SELECT name, grade FROM student''')
for row in cursor:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} : {1}'.format(row[0], row[1]))

     # Update user with id 1


# Delete user with id 2
id = 2
cursor.execute('''DELETE FROM student WHERE id = ? ''', (id,))
print('Student %d deleted' %id)

cursor.execute('''DROP TABLE student''')
print('student table deleted!')

db.commit()
db.close()
print('Connection to database closed')
