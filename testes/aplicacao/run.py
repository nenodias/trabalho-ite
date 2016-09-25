# -*- coding: utf-8 -*-
import os, os.path,sys, getopt
import tornado.ioloop
import tornado.web
from controller import UsersHandler, IndexHandler, RelatorioHandler

from pymongo import MongoClient

reload(sys)
sys.setdefaultencoding("latin-1")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MONGODB_DB_URL = os.environ.get('MONGODB_DB_URL') if os.environ.get('MONGODB_DB_URL') else 'mongodb://localhost:27017/'
MONGODB_DB_NAME = os.environ.get('APP_NAME') if os.environ.get('APP_NAME') else 'users'
 
client = MongoClient(MONGODB_DB_URL)
db = client[MONGODB_DB_NAME]

settings = {
    "debug": False,
    "template_path": r"templates/",
    "static_path": os.path.join(BASE_DIR, 'static'),
    "static_url_prefix": "/static/",
    "db":db
    }

def make_app():
    handlers = [
        (r"/", IndexHandler),
        (r"/users/(?P<pk>[^\/]+)?", UsersHandler),
        (r'/relatorio', RelatorioHandler)
    ]
    return tornado.web.Application(handlers, **settings)

if __name__ == "__main__":
    port = 8888 #porta padrão
    try:
        opts, args = getopt.getopt(sys.argv[1:],"p",["port="])
    except getopt.GetoptError:
        pass
    for opt, arg in opts:
        if opt in ('-p', '--port'):
            port = int(arg)
    print(port)
    app = make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()