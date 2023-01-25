from controller.action_buscar_nome import ActionBuscarNome
from controller.action_buscar_profissao import ActionBuscarProfissao
from controller.action_cadastro import ActionCadastro
from controller.action_deletar import ActionDelete


class ActionViewCadastro:
    def view_cadastro(self, request):
        body = request.json
        user_agent = request.headers["User-Agent"]

        action_controller_cadastro = ActionCadastro()
        body_validation = action_controller_cadastro.action(body)

        return {
            "status_code": 200,
            "data": {
                "validation": body_validation,
                "userAgent": user_agent
            },
            "success": True
        }

class ActionViewBuscarNome:
    def view_buscar_nome(self, request):
        body = request.json
        user_agent = request.headers["User-Agent"]

        action_controller_buscar_nome = ActionBuscarNome()
        body_validation = action_controller_buscar_nome.action(body)

        return {
            "status_code": 200,
            "data": {
                "validation": body_validation,
                "userAgent": user_agent
            },
            "success": True
        }

class ActionViewBuscarProfissao:
    def view_buscar_profissao(self, request):
        body = request.json
        user_agent = request.headers["User-Agent"]

        action_controller_buscar_profissao = ActionBuscarProfissao()
        body_validation = action_controller_buscar_profissao.action(body)

        return {
            "status_code": 200,
            "data": {
                "validation": body_validation,
                "userAgent": user_agent
            },
            "success": True
        }

class ActionViewDelete:
    def view_delete(self, request):
        body = request.json
        user_agent = request.headers["User-Agent"]

        action_controller_delete = ActionDelete()
        body_validation = action_controller_delete.action(body)

        return {
            "status_code": 200,
            "data": {
                "validation": body_validation,
                "userAgent": user_agent
            },
            "success": True
        }
