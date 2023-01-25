from models.job_repository import BancoDeDados


class ActionDelete:
    def __init__(self):
        self.bd_repositorio = BancoDeDados()

    def deletar_pessoa_por_nome(self, nome:str):
        self.bd_repositorio.deletar_pessoa(nome)


# Ele instancia a classe BancoDeDados dentro da classe 
# ActionDelete e armazena-a em uma variável de 
# instância chamada bd_repositorio. A função 
# deletar_pessoa_por_nome usa esse objeto para 
# chamar o método deletar_pessoa na classe 
# BancoDeDados, passando o nome da pessoa como 
# parâmetro. Isso permitiria deletar a pessoa do 
# banco de dados usando o nome como referência.
