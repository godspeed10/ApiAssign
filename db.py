from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root@localhost'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flaskapi'
 
mysql = MySQL(app)

