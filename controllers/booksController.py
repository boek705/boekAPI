from services.booksServices import BooksServices
import json

class Books:
	def on_get(self, req, resp):#read
		print('get request arrived')
        instance=BooksServices()
		#resp.status = falcon.HTTP_200
		resp.body = instance.read()
	# def on_post(self, req, resp):#create
	# 	print('post request arrived')
		
	# def on_delete(self, req, resp):#delete
	# 	sid = json.loads(req.stream.read())['id']
	# 	print(sid)
	
	# def on_put(self, req, resp):#update
	# 	data = json.loads(req.stream.read())
	# 	print(data)