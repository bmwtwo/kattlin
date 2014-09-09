import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)

DATABASE = '/tmp/db.db'
# TODO: remove before pushing to server 
DEBUG = True
# TODO change configuration
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

@app.route('/')
def index():
  return render_template('index.html') 

@app.route('/submit', methods=['POST'])
def submit():
  street = request.form['street']
  unit = request.form['unit']
  city = request.form['city']
  email = request.form['email']

  return ('Received:<br />' +
    street + '<br />' +
    unit + '<br />' +
    city + '<br />' +
    email )

if __name__ == '__main__':
  app.run()
