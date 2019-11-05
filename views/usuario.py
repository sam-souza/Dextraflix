from flask import Blueprint, jsonify, request, abort
from models.usuario import UsuarioSchema
from marshmallow.exceptions import ValidationError
# from controllers import usuario as usuario_controller

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuarios/', methods=['POST'])
def save_user():
    try:
        data = request.get_json()
        usuario_schema = UsuarioSchema()
        usuario = usuario_schema.load(data)
        # usuario_controller.save_user(usuario)

    except ValidationError:
        abort(400)