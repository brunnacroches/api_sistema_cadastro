from models.job_repository import BancoDeDados, PessoaModel


class ActionCadastro:
    def __init__(self):
        self.bd_repositorio = BancoDeDados()
    
    def inserir_pessoa(self, nome:str, idade:int, sexo:str, profissao:str):
        if profissao not in ['Médico', 'Advogado', 'Contador', 'Programador']:
            # ! raise Exception
            raise Exception('Profissão inválida')

        # ! pessoa = PessoaModel(nome, idade, sexo, profissao)
        pessoa = PessoaModel(nome=nome, idade=idade, sexo=sexo, profissao=profissao)
        self.bd_repositorio.inserir_pessoa(pessoa)

