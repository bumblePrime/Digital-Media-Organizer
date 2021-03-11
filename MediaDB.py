import sqlite3
conn=sqlite3.connect('MediaCollection.sqlite')# You can choose the name of your databsae
cur=conn.cursor()
cur.execute('DROP TABLE IF EXISTS Movies')# you can name your table whatever you want
cur.execute('CREATE TABLE Movies (Name TEXT,Location TEXT)')
fname='Content.txt'
fh=open(fname)
for line in fh:
    try:
        line=line[:line.rindex('.')+1]
        name=line[line.rindex('\\')+1:].strip()
        path=line[:line.rindex('\\')].strip()
    except:
        continue
    cur.execute('SELECT Name FROM Movies WHERE Name=?',(name,))
    if cur.fetchone() is None:
        cur.execute('INSERT INTO Movies(Name,Location) VALUES (?,?)',(name,path))
    conn.commit()
cur.close()