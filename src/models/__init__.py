from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

from .AgendaModel import AgendaModel, AgendaSchema
from .AlbumModel import AlbumModel, AlbumSchema
from .ArticleModel import ArticleModel, ArticleSchema
from .NewsModel import NewsModel, NewsSchema
from .CategoryModel import CategoryModel, CategorySchema
from .GaleryModel import GaleryModel, GalerySchema
from .PageModel import PageModel, PageSchema
