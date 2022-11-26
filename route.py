from app import app
from flask import render_template, request, redirect
from connection import insert, show_all, dell

@app.route("/index")
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/contato', methods=['POST', 'GET'])
def contato():
    if request.method=='POST':
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']
        insert(email, assunto, descricao)
    return render_template("contato.html")

@app.route('/delete/<id>', methods=['POST', 'GET'])
def delete(id):
    dell(id)
    return redirect('/visualizar')



@app.route('/quemsomos')
def quem_somos():
    return render_template("quemsomos.html")


@app.route('/visualizar', methods=['POST', 'GET'])
def visualizar():
    conteudo= show_all()
    return render_template("visualizar.html", conteudo=conteudo)


@app.route('/deletar/<int:id>')
def deletar(id):
    dell(id)
    return redirect('/visualizar')
