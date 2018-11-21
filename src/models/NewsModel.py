from . import db
from marshmallow import fields, Schema


class NewsModel(db.Model):
    """
    News Model
    """

    __tablename__ = 'berita'

    id_berita = db.Column(db.Integer, primary_key=True)
    id_kategori = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(length=50), nullable=False)
    judul = db.Column(db.String(length=82), nullable=False)
    judul_seo = db.Column(db.String(length=85), nullable=False)
    headline = db.Column(db.Enum("Y", "N"))
    isi_berita = db.Column(db.Text, nullable=False)
    gambar = db.Column(db.String(length=100), nullable=False)
    nama_lengkap = db.Column(db.String(length=100), nullable=False)
    publish = db.Column(db.Enum("Y", "N"))
    hari = db.Column(db.String(length=20), nullable=False)
    tanggal = db.Column(db.Date)
    jam = db.Column(db.Time)
    dibaca = db.Column(db.Integer)
    tag = db.Column(db.String(length=200), nullable=False)

    def __init__(self, data):
        """
        Class contructor
        """
        self.id_kategori = data.get('id_kategori')
        self.username = data.get('username')
        self.judul = data.get('judul')
        self.judul_seo = data.get('judul_seo')
        self.headline = data.get('headline')
        self.isi_berita = data.get('isi_berita')
        self.gambar = data.get('gambar')
        self.nama_lengkap = data.get('nama_lengkap')
        self.publish = data.get('publish')
        self.hari = data.get('hari')
        self.tanggal = data.get('tanggal')
        self.jam = data.get('jam')
        self.dibaca = data.get('dibaca')
        self.tag = data.get('tag')

    @staticmethod
    def get_all_news():
        return NewsModel.query.all()

    @staticmethod
    def get_news_by_id(news_id):
        return NewsModel.query.get(news_id)

    @staticmethod
    def get_news_by_category(category_id):
        return NewsModel.query.filter_by(id_kategori=category_id).all()


class NewsSchema(Schema):
    id_kategori = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    judul = fields.Str(required=True)
    judul_seo = fields.Str(required=True)
    headline = fields.Str(required=True)
    isi_berita = fields.Str(required=True)
    gambar = fields.Str(required=True)
    nama_lengkap = fields.Str(required=True)
    publish = fields.Str(required=True)
    hari = fields.Str(required=True)
    tanggal = fields.Str(required=True)
    jam = fields.Str(required=True)
    dibaca = fields.Int(required=True)
    tag = fields.Str(required=True)
