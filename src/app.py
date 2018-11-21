from flask import Flask
from .config import app_config
from .models import db

from .views.AgendaView import agenda_api as agenda_blueprint
from .views.AlbumView import album_api as album_blueprint


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

    @app.route('/', methods=['GET'])
    def index():
        """
            example endpoint
            """
        return 'Congratulations! Your part 2 endpoint is working'

    return app
