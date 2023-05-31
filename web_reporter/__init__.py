from flask import Flask, render_template

from web_reporter.config import Config
from web_reporter.main import main_app


def page_not_found(e):
    return render_template('404.html'), 404


def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object(Config)

    app.register_blueprint(main_app)
    app.register_error_handler(404, page_not_found)

    return app
