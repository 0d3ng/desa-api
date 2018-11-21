from flask import Blueprint
from flask_jsonpify import jsonify
from flask_restful import request

from ..models.GaleryModel import GaleryModel, GalerySchema
from ..util import response_message

galery_api = Blueprint('galery_api', __name__)
galery_schema = GalerySchema()


@galery_api.route('/', methods=['GET'])
def get_all_galeries():
    """
    Get all galeries
    """
    galeries = GaleryModel.get_all_galeries()
    ser_galeries = galery_schema.dump(galeries, many=True).data
    res = response_message(200, 'Success', request.url, None, ser_galeries)
    return jsonify(res)


@galery_api.route('/<int:id_galery>', methods=['GET'])
def get_galery_by_id(id_galery):
    galery = GaleryModel.get_galeri_by_id(id_galery)
    if not galery:
        res = response_message(404, 'Fail', request.url, 'Galery not found', None)
        return jsonify(res)
    ser_galery = galery_schema.dump(galery).data
    res = response_message(200, 'Success', request.url, None, ser_galery)
    return jsonify(res)
