#pip install Flask
#pip install Flask-SQLAlchemy
#pip install Flask-Migrate
#pip install Flask-Script
#pip install pymysql
#flask db init
#flask db migrate -m "Migração inical"
#flask db upgrade


from flask import Flask, render_template, request, flash, redirect
app = Flask(__name__)
from database import db
from flask_migrate import Migrate
from models import Usuario

app.config['SECRET_KEY'] = 'JHG8BJXKSAJK-0j-JKhjn87'

# drive://usuario.senha@servidor/banco_de_dados

conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/flaskG2"

app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/alunos")
def carros():
    alu = Alunos.query.all()
    return render_template("alunos.html", dados=alu)

@app.route("/alunos/add")
def alunos_add():
    return render_template("alunos_add.html")

@app.route("/alunos/save", methods=["POST"])
def save():
    nome = request.form.get("nome")
    matricula = request.form.get("matricula")
    idade = request.form.get("idade")
    if nome and matricula and idade:
        alunos = Alunos(nome, matricula, idade)
        db.session.add(alunos)
        db.session.commit()
        flash("Aluno cadastrado")
        return redirect('/alunos')
    else:
        flash("Preencha todos os campos")
        return redirect('/alunos/add')
    
@app.route("/alunos/remove/<int:id>")
def alunos_remove(id):
    alunos = Alunos.query.get(id)
    if alunos:
        db.session.delete(alunos)
        db.session.commit()
        flash("Aluno removido!!")
        return redirect("/alunos")
    else:
        flash("Caminho Incorreto!!")
        return redirect("/alunos")

@app.route("/alunos/edit/<int:id>")
def alunos_edit(id):
    try:
        alunos = Alunos.query.get(id)
        return render_template("alunos_edit.html", dados=alunos)
    except:
        flash("Aluno Inválido")
        return redirect("/alunos")
    
@app.route("/alunos/editsave", methods=["POST"])
def alunos_edit_save():
    id = request.form.get("id")
    nome = request.form.get("nome")
    matricula = request.form.get("matricula")
    idade = request.form.get("idade")

    if id and nome and matricula and idade:
        alunos = Alunos.query.get(id)
        alunos.nome = nome
        carro.matricula = matricula
        carro.idade = idade
        db.session.commit()
        flash("Dados alterados com sucesso!!")
        return redirect("/alunos")
    else:
        flash("Preencha todas as informações")
        return redirect("/alunos/edit")
    
    
if __name__ == '__main__':
    app.run()