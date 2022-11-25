import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='B#nco1234567',
    database='contatos',
)
cursor= conexao.cursor()

def insert(email, assunto, descricao):
    inserir= f'INSERT INTO contatos (email, assunto, descricao) VALUES ("{email}","{assunto}","{descricao}")'
    cursor.execute(inserir)
    conexao.commit()
    return 

def show_all():
    selecionar= f'SELECT * FROM contatos'
    cursor.execute(selecionar)
    conteudo = cursor.fetchall()
    return conteudo


def dell(id):
    id = int(id)
    deletar=f'DELETE FROM contatos WHERE id={id}'
    cursor.execute(deletar)
    conexao.commit()
    return 