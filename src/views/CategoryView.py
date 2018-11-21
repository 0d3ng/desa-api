from flask import Blueprint
from flask_jsonpify import jsonify
from flask_restful import request

from ..models.CategoryModel import CategoryModel, CategorySchema
from ..util import response_message

category_api = Blueprint('category_api', __name__)
category_schema = CategorySchema()


@category_api.route('/', methods=['GET'])
def get_all_categories():
    """
    Get all categories
    """

    categories = CategoryModel.get_all_categories()
    ser_categories = category_schema.dump(categories, many=True).data
    res = response_message(200, 'Success', request.url, None, ser_categories)
    return jsonify(res)
