from flask import json, Response, Blueprint
from ..models.PageModel import PageModel, PageSchema

page_api = Blueprint('page_api', __name__)
page_schema = PageSchema()


@page_api.route('/', methods=['GET'])
def get_all_pages():
    """
    Get all pages
    """
    pages = PageModel.get_all_pages()
    ser_pages = page_schema.dump(pages, many=True).data
    return custom_response(ser_pages, 200)


@page_api.route('/<int:page_id>', methods=['GET'])
def get_page_by_id(page_id):
    page = PageModel.get_page_by_id(page_id)
    if not page:
        return custom_response({'error': 'page not found'}, 404)
    ser_page = page_schema.dump(page).data
    return custom_response(ser_page, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
