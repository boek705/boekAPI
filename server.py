from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL,MySQLdb
from flask_cors import CORS
from controllers import booksController
app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='boek'
mysql = MySQL(app)

import routes

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)