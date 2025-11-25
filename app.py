from flask import Flask, render_template,request, redirect
from pymongo import MongoClient
from models import Lanche, Bebida
# Cria o App Flask
app = Flask(__name__)

# Tenta fazer conexão com MongoDB. Se falhar exibe a exceção (tipo de erro)
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client['hamburgueria_db']
    # Podemos usar uma coleção genérica para todos os itens
    colecao_itens = db['itens_cardapio'] 
    print("Conectado ao MongoDB!")
except Exception as e:
    print(f"Erro ao conectar: {e}")

@app.route('/')
def index():
    # Busca todos os itens (lanches e bebidas misturados)
    itens_banco = list(colecao_itens.find())
    return render_template('index.html', itens=itens_banco)

if __name__ == '__main__':
    app.run(debug=True)


