from flask import Blueprint
from flask_jsonpify import jsonify
from flask_restful import request

from ..models.AlbumModel import AlbumModel, AlbumSchema
from ..util import response_message

album_api = Blueprint('album_api', __name__)
album_schema = AlbumSchema()


@album_api.route('/', methods=['GET'])
def get_all_album():
    """
    Get all album
    """
    albums = AlbumModel.get_all_album()
    ser_albums = album_schema.dump(albums, many=True).data
    res = response_message(200, 'Success', request.url, None, ser_albums)
    return jsonify(res)
