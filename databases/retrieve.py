import sqlite3

conn = sqlite3.connect('people.db')
c = conn.cursor()
c.execute('select * from students')
print(c.fetchall())