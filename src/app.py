
from flask import Flask, render_template

app=Flask(__name__)


@app.route('/')
def index():
    titulo='IEVN'
    list=['pedro', 'mario', 'dario']

    return render_template("index.html", titulo=titulo, list=list)

@app.route('/hola')
def hola():
    return "Hola"

@app.route("/user/<string:usuario>")
def usuario(usuario):
    return "Hola como estas: "+usuario

@app.route("/numero/<int:n>")
def numero(n): 
    return "Numeros {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return "ID: {}  |  Nombre {} ".format(id, username)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma es :{}".format(n1+n2)

@app.route("/default")
@app.route("/default/<string:n>")
def default(n='juan'):
    return "el valor de n es "+n

if __name__=="__main__":
    app.run(debug=True)