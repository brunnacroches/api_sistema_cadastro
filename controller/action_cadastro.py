from main.server.routes import PessoaModel
from models.job_repository import BancoDeDados


class ActionCadastro:
    def __init__(self):
        self.bd_repositorio = BancoDeDados()
    
    def inserir_pessoa(self, nome:str, idade:int, sexo:str, profissao:str):
        if profissao not in ['Médico', 'Advogado', 'Contador', 'Programador']:
            raise ValueError('Profissão inválida')
        pessoa = PessoaModel(nome, idade, sexo, profissao)
        self.bd_repositorio.inserir_pessoa(pessoa)

