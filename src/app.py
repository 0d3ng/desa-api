from flask import Flask
from .config import app_config
from .models import db

from .views.AgendaView import agenda_api as agenda_blueprint
from .views.AlbumView import album_api as album_blueprint
from .views.ArticleView import article_api as article_blueprint
from .views.NewsView import news_api as news_blueprint
from .views.CategoryView import category_api as category_blueprint
from .views.GaleryView import galery_api as galery_blueprint
from .views.PageView import page_api as page_blueprint


def create_app(env_name):
    """
    Create app
    """

    app = Flask(__name__)
    app.config.from_object(app_config[env_name])
    print(app.config)
    db.init_app(app)
    app.register_blueprint(agenda_blueprint, url_prefix='/api/v1/agendas')
    app.register_blueprint(album_blueprint, url_prefix='/api/v1/albums')
    app.register_blueprint(article_blueprint, url_prefix='/api/v1/articles')
    app.register_blueprint(news_blueprint, url_prefix='/api/v1/news')
    app.register_blueprint(category_blueprint, url_prefix='/api/v1/categories')
    app.register_blueprint(galery_blueprint, url_prefix='/api/v1/galeries')
    app.register_blueprint(page_blueprint, url_prefix='/api/v1/pages')

    @app.route('/', methods=['GET'])
    def index():
        """
            example endpoint
            """
        return 'Congratulations! Your part 2 endpoint is working'

    return app
