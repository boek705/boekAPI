from services.booksServices import BooksServices

class BooksController:
    def getAllBooks(self,request,mysql):
        service_object = BooksServices()
        return service_object.getAllBooks(request,mysql)
    
    def getBookDetails(self,request,mysql):
        service_object = BooksServices()
        return service_object.getBookDetails(request,mysql)
    