from . import db
from marshmallow import fields, Schema


class AgendaModel(db.Model):
    """
    Agenda Model
    """

    __tablename__ = 'agenda'

    id_agenda = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    tema = db.Column(db.String(200), nullable=False)
    tema_seo = db.Column(db.String(200), nullable=False)
    isi_agenda = db.Column(db.Text, nullable=False)
    tempat = db.Column(db.String(100), nullable=False)
    pengirim = db.Column(db.String(100), nullable=False)
    tgl_mulai = db.Column(db.Date)
    tgl_selesai = db.Column(db.Date)
    tgl_posting = db.Column(db.Date)
    jam = db.Column(db.String(100))
    gambar = db.Column(db.String(100))

    def __init__(self, data):
        """
        Class constructor
        """
        self.username = data.get('username')
        self.tema = data.get('tema')
        self.tema_seo = data.get('tema_seo')
        self.isi_agenda = data.get('isi_agenda')
        self.tempat = data.get('tempat')
        self.pengirim = data.get('pengirim')
        self.tgl_mulai = data.get('tgl_mulai')
        self.tgl_selesai = data.get('tgl_selesai')
        self.tgl_posting = data.get('tgl_posting')
        self.jam = data.get('jam')
        self.gambar = data.get('gambar')

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_agenda():
        return AgendaModel.query.all()

    def __repr__(self):
        return '<id{}>'.format(self.id_agenda)


class AgendaSchema(Schema):
    id_agenda = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    tema = fields.Str(required=True)
    tema_seo = fields.Str(required=True)
    isi_agenda = fields.Str(required=True)
    tempat = fields.Str(required=True)
    pengirim = fields.Str(required=True)
    tgl_mulai = fields.Date(required=True)
    tgl_selesai = fields.Date(required=True)
    tgl_posting = fields.Date(required=True)
    jam = fields.Str(required=True)
    gambar = fields.Str(required=True)
