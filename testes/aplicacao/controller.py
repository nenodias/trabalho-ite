# -*- coding: utf-8 -*-
import tornado.web
import json
import hashlib
from tornado.escape import json_encode

from bson import json_util
from bson.objectid import ObjectId

from relatorio import gerar_pdf
from validation import validate_user

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

    def prepare(self):
        self.db = self.settings['db']

    def post(self, pk=None):
        self.set_header("Content-Type", "application/json")
        user_data = json.loads(self.request.body, encoding= "ISO-8859-1")
        try:
            validate_user(user_data)
            user_id = self.db.users.insert(user_data)
            print('User created with id ' + str(user_id))
            self.set_status(201)
        except Exception as ex:
            message = {}
            message['message'] = str(ex)
            self.write( json_util.dumps(message) )
            self.set_status(500)

    def get(self, pk=None):
        self.set_header("Content-Type", "application/json")
        self.set_status(200)
        if not pk:
            users = self.db.users.find()
            self.write( json.dumps( list(users), default=json_util.default ) )
        else:
            user = self.db.users.find({"_id" : ObjectId(pk) })
            self.write( json_util.dumps(user) )


    def delete(self, pk=None):
        if pk:
            self.db.users.remove({"_id" : ObjectId(pk) })
            self.set_status(200)
        else:
            self.set_status(500)

