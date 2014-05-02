import cherrypy
import json
import urllib
import html5lib

class HelloWorld(object):
	def index(self):
		a_query = Query()
		text = a_query.search()
		return text
	index.exposed = True

class Query():
	def search(self):
		url = 'http://www.google.com/'
		data = urllib.urlopen(url)
		# document = html5lib.parse(data)
		return data

cherrypy.config.update({'server.socket_host': '127.0.0.1', 'server.socket_port': 9999 })
cherrypy.quickstart(HelloWorld())