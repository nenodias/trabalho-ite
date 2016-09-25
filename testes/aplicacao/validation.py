from jsonschema import validate, FormatChecker

checker = FormatChecker()

schema = {
    "type" : "object",
    "properties" : {
        "nome" : {"type" : "string"},
        "email" : {"type" : "string"},
        "data_nascimento" : {"type": "string", "format": "date-time" },
        "cpf" : {"type" : "string"},
    },
}

def validate_user(user):
    return validate(user, schema, format_checker=checker)