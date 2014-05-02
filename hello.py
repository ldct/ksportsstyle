import os

import webapp2
import jinja2

class MainPage(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        template_values = {}
        self.response.write(template.render(template_values))

class About(webapp2.RequestHandler):

    def get(self):
        self.response.write('<h1> About KSportsStyle')

class Superga(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('superga.html')
        template_values = {}
        self.response.write(template.render(template_values))

class BSC(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('bsc.html')
        template_values = {}
        self.response.write(template.render(template_values))

class Mitre(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('mitre.html')
        template_values = {}
        self.response.write(template.render(template_values))

class About(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('about.html')
        template_values = {}
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/about', About),
    ('/superga', Superga),
    ('/BSC', BSC),
    ('/mitre', Mitre),
    ('/about', About),

], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)