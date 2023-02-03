from controller.action_buscar_profissao import ActionBuscarProfissao

class ActionViewBuscarProfissao:
    def view_buscar_profissao(self, request):
        # ! profissao = request.json
        # ! user_agent = request.headers["User-Agent"]
        body = request.json 
        profissao = body["profissao"] # ~ informaçõe extraídas da requisição em formato JSON

        action_controller_buscar_profissao = ActionBuscarProfissao()
        # ! profissao_validation = action_controller_buscar_profissao.buscar_pessoas_por_profissao(profissao)
        pessoas = action_controller_buscar_profissao.buscar_pessoas_por_profissao(profissao)
    
        return {
            "status_code": 200,
            # ! "data": {
            # !     "validation": profissao_validation,
            # !     "userAgent": user_agent
            # ! },
            "data": {
                "pessoas": pessoas, 
            },
            "success": True
        }

class ActionViewDelete:
    def view_delete(self, request):
        # ! nome = request.json
        # ! user_agent = request.headers["User-Agent"]
        body = request.json
        delete = body["delete"]

        action_controller_delete = ActionDelete()
        # ! nome_validation = action_controller_delete.deletar_pessoa_por_nome(nome)
        delete = action_controller_delete.deletar_pessoa_por_nome(delete)

        return {
            "status_code": 200,
            # ! "data": {
            # !     "validation": nome_validation,
            # !     "userAgent": user_agent
            # ! },
            "data" : "",
            "success": True
        }
