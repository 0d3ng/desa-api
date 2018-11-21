from flask import Blueprint
from flask_jsonpify import jsonify
from flask_restful import request

from ..models.PageModel import PageModel, PageSchema
from ..util import response_message

page_api = Blueprint('page_api', __name__)
page_schema = PageSchema()


@page_api.route('/', methods=['GET'])
def get_all_pages():
    """
    Get all pages
    """
    pages = PageModel.get_all_pages()
    ser_pages = page_schema.dump(pages, many=True).data
    res = response_message(200, 'Success', request.url, None, ser_pages)
    return jsonify(res)


@page_api.route('/<int:page_id>', methods=['GET'])
def get_page_by_id(page_id):
    page = PageModel.get_page_by_id(page_id)
    if not page:
        return response_message(404, 'Fail', request.url, 'Page not found', None)
    ser_page = page_schema.dump(page).data
    res = response_message(200, 'Success', request.url, None, ser_page)
    return jsonify(res)
