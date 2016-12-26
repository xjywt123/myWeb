import web
from web import form
urls = ('/','index')
app = web.application(urls,globals())
my_render = web.template.render('templates/',base = "layout")
class index(object):
	def GET(self):
		return my_render.hello_input()
	def POST(self):
		# form = web.input(name = "nobody",age = "28")
		# return my_render.hello("good morning!")
		x = web.input(pic = {})
		file_dir = 'F:/myRepository/myWeb/myWeb/myPic'
		# web.debug(x['pic'].filename)
		if "pic" in x:
			file_path = x.pic.filename.replace('\\','/')
			file_name = file_path.split('/')[-1]
			fout = open(file_dir+'/'+file_name,'wb')
			fout.write(x.pic.file.read())
			fout.close()
			return web.seeother('/')
		else:
			raise web.seeother('/')

if __name__ == "__main__":
	
	app.run()
