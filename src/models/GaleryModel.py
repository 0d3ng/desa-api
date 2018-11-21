from . import db
from marshmallow import fields, Schema


class GaleryModel(db.Model):
    """
    Galery Model
    """

    __tablename__ = 'galeri'

    id_galeri = db.Column(db.Integer, primary_key=True)
    id_album = db.Column(db.Integer, nullable=False)
    judul_galeri = db.Column(db.String(length=100), nullable=False)
    galeri_seo = db.Column(db.String(length=100), nullable=False)
    keterangan = db.Column(db.String(length=200), nullable=False)
    foto = db.Column(db.String(length=100), nullable=False)

    def __init__(self, data):
        """
        Class constructor
        """
        self.id_album = data.get('id_album')
        self.judul_galeri = data.get('judul_galeri')
        self.galeri_seo = data.get('galeri_seo')
        self.keterangan = data.get('keterangan')
        self.foto = data.get('foto')

    @staticmethod
    def get_all_galeries():
        return GaleryModel.query.all()

    @staticmethod
    def get_galeri_by_id(id_galery):
        return GaleryModel.query.get(id_galery)


class GalerySchema(Schema):
    id_galeri = fields.Int(dump_only=True)
    id_album = fields.Int(required=True)
    judul_galeri = fields.Str(required=True)
    galeri_seo = fields.Str(required=True)
    keterangan = fields.Str(required=True)
    foto = fields.Str(required=True)
