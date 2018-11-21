from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

from .AgendaModel import AgendaModel, AgendaSchema
from .AlbumModel import AlbumModel, AlbumSchema
