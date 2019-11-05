from main import mongo

def save_user(usuario):
    usuario["_id"] = usuario["email"]
    mongo.db.usuario.insert_one(usuario)

