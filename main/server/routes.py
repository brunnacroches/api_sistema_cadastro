from flask import jsonify, request
from views.action_view_cadastro import ActionCadastro
from views.action_view_buscar_nome import ActionBuscarNome
from views.action_view_buscar_profissao import ActionBuscarProfissao
from views.action_view_delete import ActionDelete
from .server import app

# ? POST PARA CRIAR UM NOVO RECURSO
# ! @app.route("/rota1/cadastrar", methods=["GET"])
@app.route("/rota1/cadastrar", methods=["POST"])
def route_cadastro():
    action_view = ActionCadastro()

    # ! http_response = action_view.action(request)
    http_response = action_view.inserir_pessoa(request)

    return jsonify(http_response["data"]), http_response["status_code"]

# ? POST PARA CRIAR UM NOVO RECURSO
@app.route("/rota1/buscarnome", methods=["POST"])
def route_buscar_nome():
    action_view = ActionBuscarNome()

    # ! http_response = action_view.action(request)
    http_response = action_view.buscar_pessoa_por_nome(request)

    return jsonify(http_response["data"]), http_response["status_code"]

# ? POST PARA CRIAR UM NOVO RECURSO
@app.route("/rota1/buscarprofissao", methods=["POST"])
def route_buscar_profissao():
    action_view = ActionBuscarProfissao()

    # ! http_response = action_view.action(request)
    http_response = action_view.buscar_pessoas_por_profissao(request)

    return jsonify(http_response["data"]), http_response["status_code"]

# ? POST PARA DELETAR UM NOVO RECURSO EXISTENTE
@app.route("/rota1/delete", methods=["DELETE"])
def route_delete():
    action_view = ActionDelete()

    # ! http_response = action_view.action(request)
    http_response = action_view.deletar_pessoa_por_nome(request)
    
    return jsonify(http_response["data"]), http_response["status_code"]
