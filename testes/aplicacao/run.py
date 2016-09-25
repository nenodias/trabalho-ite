# -*- coding: utf-8 -*-
import os, os.path,sys, getopt
import tornado.ioloop
import tornado.web
from controller import MainHandler, IndexHandler, RelatorioHandler

reload(sys)
sys.setdefaultencoding("latin-1")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings = {
    'debug': False,
    "template_path": r"templates/",
    "static_path": os.path.join(BASE_DIR, 'static'),
    "static_url_prefix": "/static/",
    }

def make_app():
    handlers = [
        (r"/", IndexHandler),
        (r"/users", MainHandler),
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