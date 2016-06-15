# blog.py - controller

#imports
import flask
import sqlite3

#configuration
DB = 'blog.db'

app = flask.Flask(__name__)

#pulls in app config by looking for Uppercase variables
app.config.from_object(__name__)

#function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DB'])

if __name == '__main__':
    app.run(debug=True)
