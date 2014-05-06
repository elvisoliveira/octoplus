import model
# http://lxml.de/
import lxml.html
# https://github.com/wolever/pprintpp 
import pprintpp 
# https://github.com/quandyfactory/dicttoxml
import dicttoxml 

# controller receives the model data, and threats it, to be delivered in XML
class OctoPlusController(object):
	def __init__(self):
		# 9GAG URL
		self.model = model.OctoPlusModel()

	# get one start list of articles
	def getStart(self):
		elements = self.model.getStart()
		# define dictionary for articles
		articles = {}
		# loop all articles
		for element in elements:
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