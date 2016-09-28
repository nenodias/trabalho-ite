from jsonschema import validate, FormatChecker
from datetime import datetime, date

checker = FormatChecker()

schema = {
    "type" : "object",
    "properties" : {
        "nome" : {"type" : "string"},
        "email" : {"type" : "string"},
        "data_nascimento" : {"type": "string" },
        "cpf" : {"type" : "string"},
    },
}

def validate_user(user):
    retorno = validate(user, schema, format_checker=checker)
    user["data_nascimento"] = datetime.strptime(user["data_nascimento"],'%d/%m/%Y')
    return retorno

def serializar(user):
    dado = {}
    dado['_id'] = str(user['_id'])
    dado['nome'] = user['nome'].encode('utf-8')
    dado['email'] = user['email'].encode('utf-8')
    if isinstance(user['data_nascimento'], datetime):
        dado['data_nascimento'] = datetime.strftime(user['data_nascimento'],'%d/%m/%Y')
    dado['cpf'] = user['cpf'].encode('utf-8')
    return dado