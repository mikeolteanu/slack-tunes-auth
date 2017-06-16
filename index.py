import jinja2
import urllib
import os
import json
import config
import webapp2
from google.appengine.api import urlfetch

class index(webapp2.RequestHandler):
	def get(self):
		template_values = {}
		template_values['step1']            = True
		template_values['client_id']        = config.client_id
		template_values['scope']            = config.scope
		template_values['redirect_uri']     = config.redirect_uri
		template = jinja_environment.get_template('index.html')
		self.response.out.write(template.render(template_values))

class callback(webapp2.RequestHandler):
	def get(self):
		template_values = {}
		code          = self.request.get('code')
		state         = self.request.get('state')
		client_id     = config.client_id
		client_secret = config.client_secret
		redirect_uri  = config.redirect_uri
		try :
			result = urlfetch.fetch(
				url="https://slack.com/api/oauth.access",
				payload = urllib.urlencode({
					'client_id': client_id,
					'client_secret': client_secret,
					'code': code,
                    'redirect_uri': redirect_uri
				}),
				method=urlfetch.POST,
				validate_certificate = True
			)
			json_response = json.loads(result.content)
			if result.status_code == 200 and 'access_token' in json_response:
				template_values['step2'] = True
				template_values['access_token'] = json_response['access_token']
			else:
				template_values['error'] = True
		except urlfetch.Error:
			template_values['error'] = True
		template = jinja_environment.get_template('index.html')
		self.response.out.write(template.render(template_values))

jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True
)
app = webapp2.WSGIApplication(
	[
		('/', index),
		('/callback', callback),
	]
)
