import sqlite3


conn = sqlite3.connect('people.db')

c = conn.cursor()

# create table
c.execute('CREATE TABLE students (name text, age integer)')

# insert row of data
s = ('Jeff', 23)
c.execute('INSERT INTO students VALUES (?, ?)', s)

# save (commit) the changes
conn.commit()

conn.close()