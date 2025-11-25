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

# Rota principal 
@app.route('/')
def index():
    # Busca todos os itens (lanches e bebidas misturados)
    itens_banco = list(colecao_itens.find())
    return render_template('index.html', itens=itens_banco)

# Rota para adicionar item ao cardápio
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        tipo_item = request.form['tipo_item']
        nome = request.form['nome']
        preco = float(request.form['preco'])

        # Decisão simples para verificar o tipo de item
        if tipo_item == 'lanche':
            ingredientes = request.form['ingredientes']
            novo_item = Lanche(nome, preco, ingredientes)
        
        elif tipo_item == 'bebida':
            tamanho = request.form['tamanho']
            novo_item = Bebida(nome, preco, tamanho)

        # Polimorfismo: Ambos têm o método convParaDicionario()
        colecao_itens.insert_one(novo_item.convParaDicionario())

        return redirect('/')
    
    return render_template('adicionar.html')

if __name__ == '__main__':
    app.run(debug=True)



