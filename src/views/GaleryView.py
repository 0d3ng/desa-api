from flask import json, Response, Blueprint
from ..models.GaleryModel import GaleryModel, GalerySchema

galery_api = Blueprint('galery_api', __name__)
galery_schema = GalerySchema()


@galery_api.route('/', methods=['GET'])
def get_all_galeries():
    """
    Get all galeries
    """
    galeries = GaleryModel.get_all_galeries()
    ser_galeries = galery_schema.dump(galeries, many=True).data
    return custom_response(ser_galeries, 200)


@galery_api.route('/<int:id_galery>', methods=['GET'])
def get_galery_by_id(id_galery):
    galery = GaleryModel.get_galeri_by_id(id_galery)
    if not galery:
        return custom_response({'error': 'galery no found'}, 404)
    ser_galery = galery_schema.dump(galery).data
    return custom_response(ser_galery, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
