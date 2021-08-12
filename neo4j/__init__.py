from flask import Flask


def create_app():
    from .api import api

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('neo4j.config.DefaultConfig')

    api.init_app(app)

    return app
