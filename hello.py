import urllib
import cherrypy
import lxml.html
import pprintpp
import json
import dicttoxml

# 9GAG URL
url = 'http://localhost/octoplus.html'

class OctoPlus(object):
	# main page
	def index(self):
		# get the most recent articles
		articles = self.buildvector()
		# print them on the screen		
		return dicttoxml.dicttoxml(articles)
	# get one start list of articles
	def buildvector(self):
		# read html from url, return string
		data = urllib.urlopen(url).read()
		# parse string, convert format
		# lxml document
		document = lxml.html.fromstring(data)
		# loop posts (html from srticles)
		elements = document.cssselect('article')
		# define dictionary for articles
		articles = {}
		# loop all articles
		for idx, element in enumerate(elements):
			# set article
			article = {}
			# get title
			article['title'] = element.cssselect('header h2 a')[0].text_content().strip()
			# get image image
			article['image'] = element.cssselect('img.badge-item-img')[0].get('src').strip()
			# get 9gag address
			article['address'] = element.get('data-entry-url').strip()
			# get id
			article['id'] = element.get('data-entry-id').strip()
			# get total of comments
			article['comments'] = element.cssselect('header p.post-meta a')[1].text_content().strip()
			# get total of points
			article['points'] = element.cssselect('header p.post-meta a')[0].text_content().strip()
			# fulfil dictionary
			articles[article['id']] = article
		# return dictionary
		return articles
	# expose index
	index.exposed = True

# CherryPy settings
cherrypy.config.update({'server.socket_host': '127.0.0.1', 'server.socket_port': 9999})
cherrypy.quickstart(OctoPlus())