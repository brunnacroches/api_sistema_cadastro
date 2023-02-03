from controller.action_deletar import ActionDelete


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
