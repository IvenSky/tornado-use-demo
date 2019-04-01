import tornado.web
class IndexHandler(tornado.web.RequestHandler):
	def post(self):
		self.write("post method")
	def get(self):
		self.write("get method")
