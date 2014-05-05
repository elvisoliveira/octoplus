import urllib
import cherrypy
import lxml.html

class HelloWorld(object):
    def index(self):
        url = 'http://www.9gag.com/'
        data = urllib.urlopen(url).read()
        document = lxml.html.fromstring(data)
        elements = document.cssselect('article img')
        for element in elements:
            print lxml.html.tostring(element)
        return "hello"
    index.exposed = True

cherrypy.config.update({'server.socket_host': '127.0.0.1', 'server.socket_port': 9999})
cherrypy.quickstart(HelloWorld())