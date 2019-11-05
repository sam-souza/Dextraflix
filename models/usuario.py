from marshmallow import Schema, fields, pprint
# from favorito import Favorito

class Rede(Schema):
    nome = fields.Str()
    perfil = fields.Str()

class UsuarioSchema(Schema):
    nome = fields.Str()
    email = fields.Str()
    descricao = fields.Str()
    foto = fields.Str()
    # favoritos = fields.List(fields.Nested(Favorito))
    redes = fields.List(fields.Nested(Rede))
    metadados = fields.Dict()
    admin = fields.Bool()
