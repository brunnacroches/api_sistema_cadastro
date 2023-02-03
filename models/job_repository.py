
# ! from controller.action_cadastro import ActionCadastro
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# entities arquivo separado
class PessoaModel(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    sexo = Column(String)
    profissao = Column(String)

class BancoDeDados:
    def __init__(self):
        self.engine = create_engine('sqlite:///storage.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    # ! def inserir_pessoa(self, pessoa: ActionCadastro):
    def inserir_pessoa(self, pessoa):
        session = self.Session()
        pessoa_model = PessoaModel(nome=pessoa.nome, idade=pessoa.idade, sexo=pessoa.sexo, profissao=pessoa.profissao)
        session.add(pessoa_model)
        session.commit()
        session.close()

    def buscar_pessoa_por_nome(self, nome: str):
        session = self.Session()
        pessoa_model = session.query(PessoaModel).filter_by(nome=nome).first()
        session.close()
        return pessoa_model
        # ! if pessoa_model:
        # !     return ActionCadastro(nome=pessoa_model.nome, idade=pessoa_model.idade, sexo=pessoa_model.sexo, profissao=pessoa_model.profissao)
        # ! else:
        # !     return None

    def buscar_pessoas_por_profissao(self, profissao: str):
        session = self.Session()
        pessoas_model = session.query(PessoaModel).filter_by(profissao=profissao).all()
        session.close()
        # ! pessoas = []
        # ! for pessoa_model in pessoas_model:
        # !     pessoas.append(ActionCadastro(nome=pessoa_model.nome, idade=pessoa_model.idade, sexo=pessoa_model.sexo, profissao=pessoa_model.profissao))
        return pessoas_model

    def deletar_pessoa_por_nome(self, nome: str):
        session = self.Session()
        pessoa_model = session.query(PessoaModel).filter_by(nome=nome).first()
        session.delete(pessoa_model)
        session.commit()
        session.close()


