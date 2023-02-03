from controller.action_buscar_nome import ActionBuscarNome
from controller.action_buscar_profissao import ActionBuscarProfissao
from controller.action_cadastro import ActionCadastro
from controller.action_deletar import ActionDelete
from controller.action_buscar_nome import ActionBuscarNome
from controller.action_buscar_profissao import ActionBuscarProfissao

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
