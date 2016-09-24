import tornado.web
import json
import hashlib

class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('index.html',mensagem='Bem-Vindo!')

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