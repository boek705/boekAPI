from __main__ import app,mysql
from controllers.booksController import BooksController 
from flask import Flask,render_template,request,redirect
@app.route('/')
def test():
    return 'hello'

@app.route('/getAllBooks',methods=['GET'])
def getAllBooks():
    controller_object = BooksController()
    return controller_object.getAllBooks(request,mysql)

@app.route('/getBookDetails',methods=['GET'])
def getBookDetails():
    controller_object = BooksController()
    return controller_object.getBookDetails(request,mysql)