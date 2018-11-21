from flask import Blueprint
from flask_jsonpify import jsonify
from flask_restful import request

from ..models.ArticleModel import ArticleModel, ArticleSchema
from ..util import response_message

article_api = Blueprint('article_api', __name__)
article_schema = ArticleSchema()


@article_api.route('/', methods=['GET'])
def get_all_articles():
    """
    Get all article
    """
    articles = ArticleModel.get_all_article()
    ser_articles = article_schema.dump(articles, many=True).data
    res = response_message(200, 'Success', request.url, None, ser_articles)
    return jsonify(res)


@article_api.route('/<int:id_article>', methods=['GET'])
def get_article_by_id(id_article):
    article = ArticleModel.get_article_by_id(id_article)
    if not article:
        res = response_message(404, 'Fail', request.url, 'Article not found', None)
        return jsonify(res)
    ser_article = article_schema.dump(article).data
    res = response_message(200, 'Success', request.url, None, ser_article)
    return jsonify(res)
