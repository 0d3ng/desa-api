from flask import json, Response, Blueprint, g
from ..models.ArticleModel import ArticleModel, ArticleSchema

article_api = Blueprint('article_api', __name__)
article_schema = ArticleSchema()


@article_api.route('/', methods=['GET'])
def get_all_articles():
    """
    Get all article
    """
    articles = ArticleModel.get_all_article()
    ser_articles = article_schema.dump(articles, many=True).data
    return custom_response(ser_articles, 400)


@article_api.route('/<int:id_article>', methods=['GET'])
def get_article_by_id(id_article):
    article = ArticleModel.get_article_by_id(id_article)
    if not article:
        return custom_response({'error': 'article not found'}, 404)
    ser_article = article_schema.dump(article).data
    return custom_response(ser_article, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
