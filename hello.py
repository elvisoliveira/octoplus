# system imports
import json, controller
# http://www.cherrypy.org/
import cherrypy
# https://github.com/wolever/pprintpp
import pprintpp
# https://github.com/quandyfactory/dicttoxml
import dicttoxml

class OctoPlus(object):
	# main page
	def index(self):
		controllers = controller.OctoPlusController()
		# get the most recent articles
		articles = controllers.getStart()
		# print them on the screen
		return dicttoxml.dicttoxml(articles)
	# expose index
	index.exposed = True
	def get(self, article):
		return pprintpp.pprint(article)
	get.exposed = True

# CherryPy settings
cherrypy.config.update({'server.socket_host': '127.0.0.1', 'server.socket_port': 9999})
cherrypy.quickstart(OctoPlus())