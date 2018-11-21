from flask import json, Response, Blueprint
from ..models.CategoryModel import CategoryModel, CategorySchema

category_api = Blueprint('category_api', __name__)
category_schema = CategorySchema()


@category_api.route('/', methods=['GET'])
def get_all_categories():
    """
    Get all categories
    """

    categories = CategoryModel.get_all_categories()
    ser_categories = category_schema.dump(categories, many=True).data
    return custom_response(ser_categories, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
