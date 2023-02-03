from models.job_repository import BancoDeDados


class ActionBuscarNome:
    def __init__(self):
        self.bd_repositorio = BancoDeDados()

    def buscar_pessoa_por_nome(self, nome:str)->str:
        pessoas = self.bd_repositorio.buscar_pessoa_por_nome(nome)
        return pessoas
        # ! pessoas = self.bd_repositorio.buscar_pessoas()
        # ! for pessoa in pessoas:
        # !     if pessoa.nome == nome:
        # !         return pessoa
        # ! return None

