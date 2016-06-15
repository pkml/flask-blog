# sql.py - Create a sqlite3 table and populate it with data

import sqlite3

# create a new database if the database doesnt already exist
with sqlite3.connect("blog.db") as connection:

    #get a cursor
    c = connection.cursor()

    #create the table
    c.execute("""CREATE TABLE postes(title TEXT, post TEXT)""")

    #insert dummy data
    c.execute('INSERT INTO postes VALUES("gOOD", "I\'m good.")')
    c.execute('INSERT INTO postes VALUES("Well", "I\'m well.")')
    c.execute('INSERT INTO postes VALUES("Excellent", "I\'m excellent.")')
    c.execute('INSERT INTO postes VALUES("Okey", "I\'m okey.")')
    c.execute('INSERT INTO postes VALUES("super", "I\'m super.")')
