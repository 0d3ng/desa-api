from flask import request, json, Response, Blueprint, g
from ..models.AlbumModel import AlbumModel, AlbumSchema

album_api = Blueprint('album_api', __name__)
album_schema = AlbumSchema()


@album_api.route('/', methods=['GET'])
def get_all_album():
    """
    Get all album
    """
    albums = AlbumModel.get_all_album()
    ser_albums = album_schema.dump(albums, many=True).data
    return custom_response(ser_albums, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
