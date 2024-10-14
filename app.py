import os

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

#Criando banco de dados.
ALUNOS_BANCO = create_engine ("sqlite:///alunosbanco.db")

#CRIANDO CONEXÃO COM BANCO DE DADOS
session = sessionmaker(bind=ALUNOS_BANCO)
session = session()

#Criando tabela.
Base = declarative_base()

class Aluno(Base):
    __tablename__ =  "alunos"

    #Definindo campos da tabela.
    id = Column ("id", Integer, primary_key=True, autoincrement=True)
    ra = Column("ra", String)
    nome = Column("nome", String)
    sobrenome = Column("sobrenome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    #Definindo atributos da classe
    def __init__(self, ra: str, nome: str, sobrenome: str, email: str, senha: str):
        self.ra = ra
        self.nome = nome
        self.sobrenome = sobrenome
        self. email = email
        self.senha = senha

#Criando tabela do Banco de Dados.
Base.metadata.create_all(bind=ALUNOS_BANCO)

#CRUD
#Creat - Insert - Salvar.
os.system("cls||clear")
print("= Solicitando dados para o aluno  = ")
inserir_ra = input("Digite seu R.A: ")
inserir_nome = input("Digite seu nome: ")
inserir_sobrenome = input ("Digite seu sobrenome: ")
inserir_email = input("Digite seu email: ")
inserir_senha = input("Digite sua senha: ")

aluno = Aluno(ra=inserir_ra, nome=inserir_nome, sobrenome=inserir_sobrenome, email=inserir_email, senha=inserir_senha)
session.add(aluno)
session.commit()

#R - Read - Select - Consulta 
print("\n= Exibindo dados de todos os alunos =")
lista_alunos = session.query(Aluno).all()

for aluno in lista_alunos:
    print(f"{aluno.id} - {aluno.ra} - {aluno.nome} - {aluno.sobrenome} - {aluno.email} - {aluno.senha}")

#U - Update - UPDATE -  Atualizar
print("\n= Atualizar dados de todos os usuários =")
email_aluno = input("Digite o email do aluno que será corrigido: ")

aluno = session.query(Aluno).filter_by(email = email_aluno).first()

if aluno:
    aluno.ra = input ("Digite seu R.A: ")
    aluno.nome = input("Digite seu nome: ")
    aluno.sobrenome = input("Digite seu sobrenome: ")
    aluno.email = input("Digite seu email: ")
    aluno.senha = input("Digite sua senha: ")

    session.commit

else:
    print("Aluno não encontrado!")

#R - Read - Select - Consulta 
print("\n= Exibindo dados de todos os alunos =")
lista_alunos = session.query(Aluno).all()

for alunos in lista_alunos:
    print(f"{aluno.id} - {aluno.ra} - {aluno.nome} - {aluno.sobrenome} - {aluno.email} - {aluno.senha}")

#D - Delete - DELETE - Excluir
print("\n= Excluindo os dados de um aluno =")
email_aluno = input("Digite o email do aluno que será excluído: ")

aluno = session.query(Aluno).filter_by(email = email_aluno).first()

if aluno:
    session.delete(aluno)
    session.commit()
    print(f"Aluno {aluno.nome} excluido com sucesso!")
else:
    print ("Aluno não encontrado")    

#R - Read - Select - Consulta 
print("\n= Exibindo dados de todos os alunos =")
lista_alunos = session.query(Aluno).all()

for aluno in lista_alunos:
    print(f"{aluno.id} - {aluno.ra} - {aluno.nome} - {aluno.sobrenome} - {aluno.email} - {aluno.senha}")

#R - Read - Select - Consulta
print("= Consultando os dados de apenas um aluno =")    
email_aluno = input("Digite o email do aluno: ")

aluno = session.query(Aluno).filter_by(email = email_aluno).first()

if aluno:
   print(f"{aluno.id} - {aluno.ra} - {aluno.nome} - {aluno.sobrenome} - {aluno.email} - {aluno.senha}")
else: 
    print("Aluno não encontrado")

#FECHANDO CONEXÃO COM BANCO DE DADOS    
session.close()