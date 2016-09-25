# -*- coding: utf-8 -*-
import tornado.web
import json
import hashlib
from tornado.escape import json_encode

from relatorio import gerar_pdf

class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('index.html',mensagem='Bem-Vindo!')

class RelatorioHandler(tornado.web.RequestHandler):

    def get(self):
        self.set_header("Content-Type", 'application/pdf; charset="utf-8"')
        self.set_header("Content-Disposition", 'inline; filename="filename.pdf') # Visualizar
        #self.set_header("Content-Disposition", "attachment; filename=test.pdf") # Download
        self.write(gerar_pdf().read())

class UsersHandler(tornado.web.RequestHandler):

    lista = []

    def prepare(self):
        self.set_header("Content-Type", 'application/json; charset="utf-8"')

    def post(self, pk=None):
        try:
            print(self.request.body.encode('utf-8') )
            data = json.loads(self.request.body.encode('utf-8'))
            if data.get('nome') and data.get('idade'):
                self.lista.append(data)
                md5 = hashlib.md5()
                md5.update( data['nome'] )
                print(md5.hexdigest())
                self.write('{"success":1,"message":"OK"}')
            else:
                self.write('{"success":1,"message":"Objeto não contém os atributos nome e idade "}')
        except Exception as ex:
            self.write('{"success":1,"message":"JSON não pode ser parseado %s"}'%(ex))

    def get(self, pk=None):
        print(pk)
        if self.lista:
            self.write(json.dumps(self.lista))
            for data in self.lista:
                md5 = hashlib.md5()
                md5.update( data['nome'] )
                print(md5.hexdigest())
        else:
            self.write('[]')