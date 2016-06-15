# blog.py - controller

# imports
from flask import Flask, render_template, request, session, flash, redirect, url_for, g
from functools import wraps
import sqlite3

# configuration
DB = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = '\xff\x03.\x7f\x05\x1a\xf1\x14\xec\x94UFh\xc9\xaa\x18\xed\xa7\x84\x1a\r\xf5\x93m'

app = Flask(__name__)

# pulls in app config by looking for Uppercase variables
app.config.from_object(__name__)


# function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DB'])


# wrap decorator
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


# route
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
                        request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials.'
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))
    return render_template('login.html', error=error)


@app.route('/main')
@login_required
def main():
    g.db = connect_db()
    cur = g.db.execute('select * from postes')
    postes = [dict(title=row[0], post=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('main.html', posts=postes)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))


@app.route('/add', methods=['POST'])
@login_required
def add():
    title = request.form['title']
    post =request.form['post']
    if not title or not post:
        flash("All files are required. please try again.")
        return redirect(url_for('main'))
    else:
        g.db = connect_db()
        g.db.execute('insert into postes (title, post) values (?,\
        ?)',[request.form['title'], request.form['post']])
        g.db.commit()
        g.db.close()
        flash('New entry was successfully posted!')
        return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True)
