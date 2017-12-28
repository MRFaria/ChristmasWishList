from jinja2 import Environment, FileSystemLoader

class BaseController:
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader('views'))

       
