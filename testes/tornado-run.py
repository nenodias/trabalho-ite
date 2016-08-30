# *-* coding:utf-8 *-*
import sys, getopt
import tornado.ioloop
import tornado.web
import json
import hashlib
reload(sys)
sys.setdefaultencoding("latin-1")

class MainHandler(tornado.web.RequestHandler):

    lista = []

    def post(self):
        try:
            print(self.request.body.encode('utf-8') )
            data = json.loads(self.request.body.encode('utf-8'))
            if data.get('nome') and data.get('idade'):
                MainHandler.lista.append(data)
                md5 = hashlib.md5()
                md5.update( data['nome'] )
                print(md5.hexdigest())
                self.write('{"success":1,"message":"OK"}')
            else:
                self.write('{"success":1,"message":"Objeto não contém os atributos nome e idade "}')
        except Exception as ex:
            self.write('{"success":1,"message":"JSON não pode ser parseado %s"}'%(ex))

    def get(self):
        if MainHandler.lista:
            self.write(json.dumps(MainHandler.lista))
            for data in MainHandler.lista:
                md5 = hashlib.md5()
                md5.update( data['nome'] )
                print(md5.hexdigest())
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