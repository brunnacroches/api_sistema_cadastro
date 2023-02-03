from models.job_repository import BancoDeDados


class ActionBuscarProfissao:
    def __init__(self):
        self.bd_repositorio = BancoDeDados()

    def buscar_pessoas_por_profissao(self, profissao:str)->list:
        pessoas = self.bd_repositorio.buscar_pessoas_por_profissao(profissao)

        formatted_pessoas_info = []
        for pessoa in pessoas:
            formatted_pessoas_info.append({
                "nome": pessoa.nome,
                "profissao": pessoa.profissao
            })
        return formatted_pessoas_info

        # ! pessoas_com_profissao = []
        # ! pessoas = self.bd_repositorio.buscar_pessoas()
        # ! for pessoa in pessoas:
        # !     if pessoa.profissao == profissao:
        # !         pessoas_com_profissao.append(pessoa)
        # ! return pessoas_com_profissao 
