import cherrypy
from controllers import base

class HomeController(base.BaseController):
    @cherrypy.expose
    def index(self):
        template = self.env.get_template('index.html')
        db = cherrypy.request.db
        return template.render()
        

