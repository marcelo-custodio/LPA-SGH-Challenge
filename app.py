"""
Criação do webserver em flask para API do desafio
"""

from flask import Flask
from server.routes import api_routes
from server.driver import clear_reports

app = Flask(__name__, static_folder="../webapp/build")
""" Instância principal da aplicação """

app.register_blueprint(api_routes)
""" Registro de Rotas da API """

@app.route("/site-map", methods=['GET'])
def site_map():
    return str(app.url_map)

@app.route("/", methods=['GET'])
def react_app():
    pass

if __name__ == '__main__':
    clear_reports()
    app.run(use_reloader=True, port=5000, threaded=True)