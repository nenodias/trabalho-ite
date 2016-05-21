# *-* coding:utf-8 *-*
import sys, getopt
import tornado.ioloop
import tornado.web
import json


class MainHandler(tornado.web.RequestHandler):

    lista = []

    def post(self):
        data = json.loads(self.request.body)
        MainHandler.lista.append(data)
        self.write('{"success":1,"message":"OK"}')

    def get(self):
        if MainHandler.lista:
            self.write(json.dumps(MainHandler.lista))
        else:
            self.write('[]')

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    port = 8888 #porta padrão
    try:
        '''
        Argumentos que pode receber o : é o delimitador
        '''
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