from flask import jsonify, request
from views.action_view import (ActionViewBuscarNome, ActionViewBuscarProfissao,
                               ActionViewCadastro, ActionViewDelete)

from .server import app


# ! @app.route("/rota1/cadastrar", methods=["GET"])
@app.route("/rota1/cadastrar", methods=["POST"])
def route_cadastro():
    action_view = ActionViewCadastro()

    # ! http_response = action_view.action(request)
    http_response = action_view.view_cadastro(request)

    return jsonify(http_response["data"]), http_response["status_code"]


@app.route("/rota1/buscarnome", methods=["POST"])
def route_buscar_nome():
    action_view = ActionViewBuscarNome()

    # ! http_response = action_view.action(request)
    http_response = action_view.view_buscar_nome(request)

    return jsonify(http_response["data"]), http_response["status_code"]

@app.route("/rota1/buscarprofissao", methods=["POST"])
def route_buscar_profissao():
    action_view = ActionViewBuscarProfissao()

    # ! http_response = action_view.action(request)
    http_response = action_view.view_buscar_profissao(request)

    return jsonify(http_response["data"]), http_response["status_code"]


@app.route("/rota1/delete", methods=["DELETE"])
def route_delete():
    action_view = ActionViewDelete()

    # ! http_response = action_view.action(request)
    http_response = action_view.view_delete(request)
    
    return jsonify(http_response["data"]), http_response["status_code"]
