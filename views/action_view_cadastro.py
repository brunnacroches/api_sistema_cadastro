from controller.action_cadastro import ActionCadastro

# fazer as views separadas
class ActionViewCadastro:
    def view_cadastro(self, request):
        body = request.json # recebe uma requisição (request) e extrais as inf da req em formado JSON
        # !! user_agent = request.headers["User-Agent"]
        # ? O que eu quero acessar com a requisição?
        nome = body["nome"]           # ~informações extraídas da requisição em formato JSON
        idade = body["idade"]         # ~informações extraídas da requisição em formato JSON
        sexo = body["sexo"]           # ~informações extraídas da requisição em formato JSON
        profissao = body["profissao"]   # ~informações extraídas da requisição em formato JSON
        # ~a notação colchetes para acessar o valor da chave "nome" ou "idade" etc do objeto JSON e armazenado em "body"

        action_controller_cadastro = ActionCadastro()
        # !! body_validation = action_controller_cadastro.inserir_pessoa(body)
        action_controller_cadastro.inserir_pessoa(nome, idade, sexo, profissao)
        # ~ action_controller_cadastro invoca o método inserir_pessoas na classe ActionCadastro()
        # ~ e passa como um argumento os objetos do body(nome, idade, sexo  e profissao)

        return { # ~essa função retorna um dicionário
            "status_code": 200,
            # !! "data": {
            # !!    "validation": body_validation,
            # !!    "userAgent": user_agent
            # !!},
            "data": "", # ~ está vazio e significa que não há dados a serem retornados
            "success": True # ~a operação foi bem sucessida
        }
