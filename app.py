import cherrypy
import os
from controllers import home

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
    SAEnginePlugin(cherrypy.engine, 'sqlite:///my.db').subscribe()

    # Register the SQLAlchemy tool
    from plugins.sql_alchemy.satool import SATool
    cherrypy.tools.db = SATool()

    cherrypy.quickstart(home.HomeController(), '/', conf)
