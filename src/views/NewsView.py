from flask import Blueprint
from flask_jsonpify import jsonify
from flask_restful import request

from ..models.NewsModel import NewsModel, NewsSchema
from ..util import response_message

news_api = Blueprint('news_api', __name__)
news_schema = NewsSchema()


@news_api.route('/', methods=['GET'])
def get_all_news():
    """
    Get all news
    """
    news = NewsModel.get_all_news()
    ser_news = news_schema.dump(news, many=True).data
    res = response_message(200, 'Success', request.url, None, ser_news)
    return jsonify(res)


@news_api.route('/<int:id_news>', methods=['GET'])
def get_news_by_id(id_news):
    news = NewsModel.get_news_by_id(id_news)
    if not news:
        res = response_message(404, 'Fail', request.url, 'News not found', None)
        return jsonify(res)
    ser_news = news_schema.dump(news).data
    res = response_message(200, 'Success', request.url, None, ser_news)
    return jsonify(res)


@news_api.route('/category/<int:id_category>', methods=['GET'])
def get_news_by_category(id_category):
    news = NewsModel.get_news_by_category(id_category)
    if not news:
        res = response_message(404, 'Fail', request.url, 'News not found', None)
        return jsonify(res)
    ser_news = news_schema.dump(news, many=True).data
    res = response_message(200, 'Success', request.url, None, ser_news)
    return jsonify(res)
