import xml.dom.minidom as minidom
import sqlite3 as sql

conn = sql.connect('../law.db')
cur = conn.cursor()
# minidom initialize
domtree = minidom.parse('person_pullout.xml')

group = domtree.documentElement

cur.execute("SELECT * FROM lawyers")
data = cur.fetchall()
for i in data:
    new_person = domtree.createElement("person")
    new_person.setAttribute("id", str(i[0]))

    name = domtree.createElement("name")
    name.appendChild(domtree.createTextNode(str(i[1])))

    experience = domtree.createElement("experience")
    experience.appendChild(domtree.createTextNode(str(i[2])))

    new_person.appendChild(name)
    new_person.appendChild(experience)

    group.appendChild(new_person)

with open('person_pullout.xml', 'w') as f:
    f.write(domtree.toprettyxml())




