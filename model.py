# system imports
import urllib
# http://lxml.de/
import lxml.html
# https://github.com/wolever/pprintpp
import pprintpp

# Model is the interface between 9GAG and the controller
class OctoPlusModel(object):
	def __init__(self):
		# 9GAG URL
		self.url = 'http://localhost/octoplus.html'
	
	def getStart(self):
		# read html from url, return string
		data = urllib.urlopen(self.url).read().decode('utf-8')
		# parse string, convert format
		# lxml document
		document = lxml.html.fromstring(data)
		# loop posts (html from srticles)
		elements = document.cssselect('article')
		# return the document
		return elements