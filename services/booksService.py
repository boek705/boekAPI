import mysql.connector
import json

mydb = mysql.connector.connect(host='localhost', user='root', passwd='', database='boek')
cur = mydb.cursor()

att = ['isbn','mrp','name','author','image_url','description','categories']

class BooksServices:
	def read(self):
        query="select * from books"
        cur.execute(query)
        data=[]
        for row in cur:
            jsn={}
            for i,attribute in enumerate(att):
                jsn[attribute] = row[i]
            data.append(jsn)
        return data
	# def insert(self, data):
	# 	# print(type(data))
		
	# def update(self, data):
		
	# def delete(self, sid):
		