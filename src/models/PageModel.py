from . import db
from marshmallow import fields, Schema


class PageModel(db.Model):
    """
    Page model
    """

    __tablename__ = 'halamanstatis'

    id_halaman = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(length=100), nullable=False)
    judul_seo = db.Column(db.String(length=100), nullable=False)
    isi_halaman = db.Column(db.Text, nullable=False)
    tanggal = db.Column(db.Date)
    gambar = db.Column(db.String(length=100), nullable=False)

    def __init__(self, data):
        """
        Class constructor
        """
        self.judul = data.get('judul')
        self.judul_seo = data.get('judul')
        self.isi_halaman = data.get('isi_halaman')
        self.tanggal = data.get('tanggal')
        self.gambar = data.get('gambar')

    @staticmethod
    def get_all_pages():
        return PageModel.query.all()

    @staticmethod
    def get_page_by_id(id_page):
        return PageModel.query.get(id_page)


class PageSchema(Schema):
    id_halaman = fields.Int(dump_only=True)
    judul = fields.Str(required=True)
    judul_seo = fields.Str(required=True)
    isi_halaman = fields.Str(required=True)
    tanggal = fields.Str(required=True)
    gambar = fields.Str(required=True)
