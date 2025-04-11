#1) crie uma função consulta_aluno que recebe a id de um aluno e devolve
#um dicionário com os dados desse aluno
from sqlalchemy import create_engine
from sqlalchemy.sql import text

# Custom exception for when a student is not found
class AlunoNaoExisteException(Exception):
    pass


# Configure the SQLAlchemy engine
engine = create_engine('sqlite:///biblioteca.db')  # Replace with your database URL


def consulta_aluno(id_aluno):
    with engine.connect() as con:
        sql_consulta = text("SELECT * FROM aluno WHERE id = :id_do_aluno")
        rs = con.execute(sql_consulta, {"id_do_aluno": id_aluno})
        result = rs.fetchone()
        if result is None:
            raise AlunoNaoExisteException
        return dict(result._mapping)
print("r1: ", consulta_aluno(1))



#1b) crie uma função todos_alunos que retorna uma lista com um dicionário
# para cada aluno
#sugestão copilot
#def todos_alunos():
#    with engine.connect() as con:
#        sql_consulta = text("SELECT * FROM aluno")
#        rs = con.execute(sql_consulta)
#        result = rs.fetchall()
#        return [dict(row) for row in result]
    

    
def todos_alunos():
    with engine.connect() as con:    
        sql_consulta = text ("SELECT * FROM aluno")
        rs = con.execute(sql_consulta)
        resultados = []
        while True:#que roda pra sempre
            result = rs.fetchone()
            if result == None:
                break
            d_result = dict(result._mapping)
            resultados.append(d_result)
        return resultados
print("r1b: ", todos_alunos())

#1c) crie uma função todos_livros que retorna uma lista com um dicionários
#para cada livro
def todos_livros():
    with engine.connect() as con:
        sql_consulta = text("SELECT * FROM livro")
        rs = con.execute(sql_consulta)
        resultados = []
        while True:
            result = rs.fetchone()
            if result == None:
                break
            d_result = dict(result._mapping)
            resultados.append(d_result)
        return resultados
print("r1c: ", todos_livros())

#2) crie uma função cria livro que recebe os dados de um livro(id e descrição)
#e os adiciona no banco de dados
#sugestão copilot
# def cria_livro(id_livro, descricao):
#     with engine.connect() as con:
#         sql_insert = text("INSERT INTO livro (id, descricao) VALUES (:id_livro, :descricao)")
#         con.execute(sql_insert, {"id_livro": id_livro, "descricao": descricao})
#         con.commit()
#     return {"id": id_livro, "descricao": descricao}
# print("r2: ", cria_livro(5, "livro 5"))
# print("todos livros: ", todos_livros())
def cria_livro(id_livro, descricao):
    with engine.connect() as con:
        sql_create = text("INSERT INTO livro (id_livro, descricao) VALUES (:id_livro, :descricao)")
        con.execute(sql_create, {"id_livro": id_livro, "descricao": descricao})
        con.commit()
    return {"id": id_livro, "descricao": descricao}

#3) crie uma função empresta_livro, que recebe a id de um livro, a id de um aluno
#e marca o livro como esprestado pelo aluno
def empresta_livro(id_livro, id_aluno):
    with engine.connect() as con:
        sql_update = text("UPDATE livro SET id_aluno = :id_aluno WHERE id_livro = :id_livro")
        con.execute(sql_update, {"id_aluno": id_aluno, "id_livro": id_livro})
        con.commit()
    return {"id_livro": id_livro, "id_aluno": id_aluno}

#4) crie uma função devolve_livro, que recebe a id de um livro e marca o livro
#como disponível
def devolve_livro(id_livro):
    with engine.connect() as con:
        sql_update = text("UPDATE livro SET id_aluno = NULL WHERE id_livro = :id_livro")
        con.execute(sql_update, {"id_livro": id_livro})
        con.commit()
    return {"id_livro": id_livro}

#5) crie uma função livros_parados que devolve a lista de todos os livros que não estão emprestados
def livros_parados():
    with engine.connect() as con:
        sql_select = text("SELECT * FROM livro WHERE id_aluno IS NULL")
        rs = con.execute(sql_select)
        resultados = []
        while True:
            result = rs.fetchone()
            if result == None:
                break
            d_result = dict(result._mapping)
            resultados.append(d_result)
        return resultados
print("r5: ", livros_parados())

#6) crie uma função livros_do_aluno que recebe o nome do aluno e devolve 
# a lista de todos os livros que estão com o aluno no momento
def livros_do_aluno(nome_aluno):
    with engine.connect() as con:
        sql_select = text("SELECT livro.* FROM livro JOIN aluno ON livro.id_aluno = aluno.id WHERE aluno.nome = :nome_aluno")
        rs = con.execute(sql_select, {"nome_aluno": nome_aluno})
        resultados = []
        while True:
            result = rs.fetchone()
            if result == None:
                break
            d_result = dict(result._mapping)
            resultados.append(d_result)
        return resultados
print("r6: ", livros_do_aluno("Helena O. S.")) 