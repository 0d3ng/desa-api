from . import db
from marshmallow import fields, Schema
import enum


class ActiveType(enum.Enum):
    ACTIVE = "Y"
    NOT_ACTIVE = "N"


class AlbumModel(db.Model):
    """
    Album model
    """

    __tablename__ = 'album'

    id_album = db.Column(db.Integer, primary_key=True)
    nama_album = db.Column(db.String(length=100), nullable=False)
    album_seo = db.Column(db.String(length=100), nullable=False)
    gambar = db.Column(db.String(200), nullable=False)
    aktif = db.Column(db.Enum(ActiveType))

    def __init__(self, data):
        """
        Class contructor
        """
        self.nama_album = data.get('nama_album')
        self.album_seo = data.get('album_seo')
        self.gambar = data.get('gambar')
        self.aktif = data.get('aktif')

    @staticmethod
    def get_all_album():
        return AlbumModel.query.all()


class AlbumSchema(Schema):
    id_album = fields.Int(dump_only=True)
    nama_album = fields.Str(required=True)
    album_seo = fields.Str(required=True)
    gambar = fields.Str(required=True)
    aktif = fields.Str(required=True)
