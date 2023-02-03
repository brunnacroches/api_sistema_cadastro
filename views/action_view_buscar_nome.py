from controller.action_buscar_nome import ActionBuscarNome

class ActionViewBuscarNome:
    def view_buscar_nome(self, request):
        body = request.json
        # !! user_agent = request.headers["User-Agent"]
        nome = body["nome"] #~ informações extraídas da requisição em formato JSON
        # ~ acessa o valor da chave "nome" do objeto JSON e armazena em body

        action_controller_buscar_nome = ActionBuscarNome()
        # !! body_validation = action_controller_buscar_nome.buscar_pessoa_por_nome(body)
        pessoa = action_controller_buscar_nome.buscar_pessoa_por_nome(nome)

        return {
            "status_code": 200,
            # !! "data": {
            # !!     "validation": body_validation,
            # !!     "userAgent": user_agent
            # !! },
            "data": { # ~ essa função retorna um dicionário que retorna um dicionário
                "pessoa": pessoa.nome,
                "idade": pessoa.idade
            },
            "success": True
        }
