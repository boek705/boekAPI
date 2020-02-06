from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='boek'

mysql = MySQL(app)

@app.route("/")
def index():
    return "Hello"

@app.route('/getdetails',methods=['GET'])
def get():
    if(request.method=="GET"):
        attr=["isbn","mrp","name","author","image_url","description","categories"]
        cur=mysql.connection.cursor()
        cur.execute("Select * from books")
        cur_data=cur.fetchall()
        
        fetch_list=[]
        for data in cur_data:
            dictionary={}
            for i,x in enumerate(data):
                dictionary[attr[i]]=x
            fetch_list.append(dictionary)
        print(fetch_list)
        cur.close()
        return json.dumps(fetch_list)



if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)