import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, nullable=False)
    user_to_id = Column(Integer, nullable=False)
    usuarios_id = Column(Integer, ForeignKey('usuario.id'))

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    
# class Seguidores(Base):
#     __tablename__ = 'seguidores'
#     id = Column(Integer, primary_key=True)
#     id_seguidor = Column(String(250), nullable=False)
#     usuarios_id = Column(Integer, ForeignKey('usuario.id'))

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    id_seguidor = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    id_seguidor = Column(String(250), nullable=False)
    descripcion = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('media.id'))
    
class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url = Column(String(50), nullable=False)
    post_id = Column(Integer, nullable=False)

class Comentarios(Base):
    __tablename__ = 'comentarios'
    id = Column(Integer, primary_key=True)
    comentario = Column(String(250))
    # usuario_id = Column(Integer, ForeignKey('usuario.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')