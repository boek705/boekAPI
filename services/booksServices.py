from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL,MySQLdb
import json
import urllib.parse as urlparse
from urllib.parse import parse_qs

class BooksServices:
    def getAllBooks(self,request,mysql):
        if(request.method=="GET"):
            
            cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("Select isbn,name,author,category from books")
            cur_data=cur.fetchall()

            print(cur_data)
            #cur.close()
            return json.dumps(cur_data)
            
    def getBookDetails(self,request,mysql):
        if(request.method=="GET"):
            print("Hello")
            isbn=request.args["isbn"][1:-1]
            cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("Select image_url,description,publication from books where isbn=%s",(isbn,))
            cur_data=cur.fetchall()

            print(cur_data)
            if(len(cur_data)==0):
                return json.dumps(["Not available"])
            #cur.close()
            return json.dumps(cur_data[0])


