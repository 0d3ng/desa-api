from flask import json, Response, Blueprint
from ..models.NewsModel import NewsModel, NewsSchema

news_api = Blueprint('news_api', __name__)
news_schema = NewsSchema()


@news_api.route('/', methods=['GET'])
def get_all_news():
    """
    Get all news
    """
    news = NewsModel.get_all_news()
    ser_news = news_schema.dump(news, many=True).data
    return custom_response(ser_news, 200)


@news_api.route('/<int:id_news>', methods=['GET'])
def get_news_by_id(id_news):
    news = NewsModel.get_news_by_id(id_news)
    if not news:
        return custom_response({'error': 'news not found'}, 404)
    ser_news = news_schema.dump(news).data
    return custom_response(ser_news, 200)


@news_api.route('/category/<int:id_category>', methods=['GET'])
def get_news_by_category(id_category):
    news = NewsModel.get_news_by_category(id_category)
    if not news:
        return custom_response({'error': 'news not found'}, 404)
    ser_news = news_schema.dump(news, many=True).data
    return custom_response(ser_news, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
