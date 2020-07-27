import os
from flask import Flask
from flask import jsonify
from config import ProductionConfig, TestingConfig, DevelopmentConfig
from api.utils.database import db
from api.utils.responses import response_with
import api.utils.responses as resp

from api.routes.authors import author_routes
from api.routes.books import book_routes

if os.environ.get('WORK_ENV') == 'PROD':
    app_config = ProductionConfig
elif os.environ.get('WORK_ENV') == 'TEST':
    app_config = TestingConfig
else:
    app_config = DevelopmentConfig

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(app_config)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    @app.after_request
    def add_header(response):
        return response

    @app.errorhandler(400)
    def bad_request(e):
        return response_with(resp.BAD_REQUEST_400)

    @app.errorhandler(500)
    def server_error(e):
        return response_with(resp.SERVER_ERROR_500)

    @app.errorhandler(404)
    def not_found(e):
        return response_with(resp.SERVER_ERROR_404)

    app.register_blueprint(author_routes, url_prefix='/api/authors')
    app.register_blueprint(book_routes, url_prefix='/api/books')

    return app

app = create_app(app_config)
