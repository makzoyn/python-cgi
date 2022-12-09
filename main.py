#!/usr/bin/python3
import sqlite3 as sql

print("Content-type: text/html\n\n")
print()
import cgi
import cgitb

cgitb.enable()

conn = sql.connect("law.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS lawyers(
    lawyer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    experience INTEGER NOT NULL);
""")
cur.execute("""CREATE TABLE IF NOT EXISTS specializations (
    specialization_id	INTEGER PRIMARY KEY,
    specialization	TEXT UNIQUE
);
""")
cur.execute("""CREATE TABLE IF NOT EXISTS lawyers_spec (
    lawyer_id	INTEGER NOT NULL UNIQUE,
    specialization_id	INTEGER NOT NULL,
    FOREIGN KEY(lawyer_id) REFERENCES lawyers(lawyer_id) ON DELETE CASCADE,
    FOREIGN KEY(specialization_id) REFERENCES specializations(specialization_id),
    PRIMARY KEY(lawyer_id,specialization_id)
    );
""")
conn.commit()

form = cgi.FieldStorage()
lawyer_name = form.getvalue("lawyer_name")
lawyer_exp = form.getvalue("lawyer_exp")
lawyer_spec = form.getvalue("lawyer_spec")
lawyers_data = (lawyer_name, lawyer_exp)

cur.execute("INSERT INTO lawyers(name, experience) VALUES(?,?)", lawyers_data)
conn.commit()
cur.execute("select specialization_id from specializations where specialization=?", [lawyer_spec])
spec_id = cur.fetchone()
cur.execute("select seq from sqlite_sequence where name='lawyers';")
lawyer_id = cur.fetchone()
print(lawyer_id)
spec_data = (str(lawyer_id).strip(",)("), str(spec_id))
cur.execute("INSERT INTO lawyers_spec(lawyer_id, specialization_id) VALUES(?,?)", spec_data)
conn.commit()
cur.close()

print('<h1>Your data insert!<h1>')

# юриспрюденция
