from . import db
from marshmallow import fields, Schema


class CategoryModel(db.Model):
    """
    Category model
    """

    __tablename__ = 'kategori'

    id_kategori = db.Column(db.Integer, primary_key=True)
    nama_kategori = db.Column(db.String(length=100), nullable=False)
    kategori_seo = db.Column(db.String(length=100), nullable=False)
    aktif = db.Column(db.Enum("Y", "N"))

    def __init__(self, data):
        """
        Class constructor
        """
        self.id_kategori = data.get('id_kategori')
        self.nama_kategori = data.get('nama_kategori')
        self.kategori_seo = data.get('kategori_seo')
        self.aktif = data.get('aktif')

    @staticmethod
    def get_all_categories():
        return CategoryModel.query.all()


class CategorySchema(Schema):
    id_kategori = fields.Int(dump_only=True)
    nama_kategori = fields.Str(required=True)
    kategori_seo = fields.Str(required=True)
    aktif = fields.Str(required=True)
