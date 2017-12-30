import cherrypy
from ..models import model
from jinja2 import Environment, FileSystemLoader

class BaseController:
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader('app/views'))

class HomeController(BaseController):
    @cherrypy.expose
    def index(self):
        template = self.env.get_template('index.html')
        w = model.Wishlist(value='Book1', bought=True)
        p = model.Person(name='Mauro')

        cherrypy.request.db.add(w)
        cherrypy.request.db.add(p)

        return template.render()

    @cherrypy.expose
    def lists(self, firstname):
        template = self.env.get_template('lists.html')

        mauro_gifts = {
            'name' : 'Mauro',
            'wishlist' : ['Book', 'Harp']
        }
        iris_gifts = {
            'name' : 'Iris',
            'wishlist' : ['Book1', 'Harp1']
        }
        people = [mauro_gifts, iris_gifts]
        
        return template.render(firstname=firstname, people=people)
        

