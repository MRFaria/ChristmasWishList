import cherrypy
import os
from app.controllers import controller
from app.models import model

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
            'tools.db.on' : True
        },
        '/static' : {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
    }
    # Register the SQLAlchemy plugin
    from plugins.sql_alchemy.saplugin import SAEnginePlugin
    SAEnginePlugin(cherrypy.engine, 'sqlite:///my.db', model.Base.metadata).subscribe()

    # Register the SQLAlchemy tool
    from plugins.sql_alchemy.satool import SATool
    cherrypy.tools.db = SATool()

    cherrypy.tree.mount(controller.HomeController(), '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
