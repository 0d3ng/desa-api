from . import db
from marshmallow import fields, Schema


class ArticleModel(db.Model):
    """
    Article model
    """

    __tablename__ = 'artikel'

    id_artikel = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=50), nullable=False)
    judul_artikel = db.Column(db.String(length=82), nullable=False)
    artikel_seo = db.Column(db.String(length=85), nullable=False)
    isi_artikel = db.Column(db.Text, nullable=False)
    gambar = db.Column(db.String(length=100), nullable=False)
    publish = db.Column(db.Enum("Y", "N"))
    hari = db.Column(db.String(length=20), nullable=False)
    tanggal = db.Column(db.Date)
    jam = db.Column(db.Time)
    dibaca = db.Column(db.Integer, nullable=False)
    tag_seo = db.Column(db.String(length=200), nullable=False)
    buletin = db.Column(db.Enum("Y", "N"))

    def __init__(self, data):
        """
        Class contructor
        """
        self.username = data.get('username')
        self.judul_artikel = data.get('judul_artikel')
        self.artikel_seo = data.get('artikel_seo')
        self.isi_artikel = data.get('isi_artikel')
        self.gambar = data.get('gambar')
        self.publish = data.get('publish')
        self.hari = data.get('hari')
        self.tanggal = data.get('tanggal')
        self.jam = data.get('jam')
        self.dibaca = data.get('dibaca')
        self.tag_seo = data.get('tag_seo')
        self.buletin = data.get('buletin')

    @staticmethod
    def get_all_article():
        return ArticleModel.query.all()

    @staticmethod
    def get_article_by_id(article_id):
        return ArticleModel.query.get(article_id)


class ArticleSchema(Schema):
    id_artikel = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    judul_artikel = fields.Str(required=True)
    artikel_seo = fields.Str(required=True)
    isi_artikel = fields.Str(required=True)
    gambar = fields.Str(required=True)
    publish = fields.Str(required=True)
    hari = fields.Str(required=True)
    tanggal = fields.Date(required=True)
    jam = fields.Time(required=True)
    dibaca = fields.Int(required=True)
    tag_seo = fields.Str(required=True)
    buletin = fields.Str(required=True)
