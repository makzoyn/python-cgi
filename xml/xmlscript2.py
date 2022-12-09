import xml.dom.minidom as minidom
import sqlite3 as sql

conn = sql.connect('../law.db')
cur = conn.cursor()
# minidom initialize
domtree = minidom.parse('person_in.xml')

group = domtree.documentElement

people = group.getElementsByTagName('person')

for person in people:
    name = person.getElementsByTagName('name')[0].childNodes[0].nodeValue
    experience = person.getElementsByTagName('experience')[0].childNodes[0].nodeValue
    data = (name, int(experience))
    cur.execute("INSERT INTO lawyers(name, experience) VALUES(?,?)", data)
    conn.commit()

conn.close()
