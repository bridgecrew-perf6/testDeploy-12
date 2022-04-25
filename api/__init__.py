from flask import Flask
from flask_restx import Api
from .main import math_namespace
from.config import config_dist
from werkzeug.exceptions import NotFound, MethodNotAllowed, InternalServerError


def create_app(config=config_dist['prod']):
    app=Flask(__name__)

    api= Api(app,
        title='Python-assessment',
        description='Klarna - Invitation to complete coding assessment'
    )

    app.config.from_object(config)

    # api.add_namespace(math_namespace, path="/")
    api.add_namespace(math_namespace)

    @api.errorhandler(NotFound)
    def not_found(error):
        return {"error":"Not foud"}, 404

    @api.errorhandler(MethodNotAllowed)
    def method_not_allowed(error):
        return {"error":"Method not allowed"}, 405

    @api.errorhandler(InternalServerError)
    def internal_server_error(error):
        return {'error':'Internal server error'}, 500

    return app