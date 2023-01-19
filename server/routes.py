"""
Controle de rotas da aplicação

"""
from flask import Blueprint
from server.apps.reports.views import bp as reports_routes
from server.apps.files.views import bp as files_routes

api_routes = Blueprint('api', __name__, url_prefix='/api')
api_routes.register_blueprint(reports_routes)
api_routes.register_blueprint(files_routes)