from models.usuario import Usuario
from models import db

def obtener_usuarios():
    return Usuario.query.all()

def agregar_usuario(data):
    nuevo_usuario = Usuario(nombre= data['nombre'], email= data['email'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return "Usuario agregado correctamente :) "


def actualizar_usuario(id, nombre, email):
    usuario = Usuario.query.get(id)
    usuario.nombre = nombre
    usuario.email = email
    db.session.commit()
    return "Usuario actualizado correctamente :) "

def eliminar_usuario(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return "Usuario eliminado correctamente :) "

