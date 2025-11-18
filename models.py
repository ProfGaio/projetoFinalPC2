class Lanche:
    def __init__(self,nome,preco,ingredientes):
        self.nome = nome
        self.preco = preco

        # Verificação se "ingredientes" é uma lista
        if isinstance(ingredientes, str):
            self.ingredientes = [item.strip() 
                for item in ingredientes.split(",") ]
        else:
            self.ingredientes = ingredientes

    def convParaDicionario(self):
        """
        Prepara o objeto para ser gravado no MongoDB,
        tornando-o um dicionário.
        """
        return{
            "tipo":"lanche",
            "nome":self.nome,
            "preco":self.preco,
            "ingredientes":self.ingredientes
        }
    
class Bebida:
    def __init__(self, nome, preco, tamanhoMl):
        self.nome = nome
        self.preco = preco
        self.tamanhoMl = tamanhoMl
    
    def convParaDicionario(self):
        """
        Prepara o objeto para ser gravado no MongoDB,
        tornando-o um dicionário.
        """
        return{
            "tipo":"bebida",
            "nome":self.nome,
            "preco":self.preco,
            "tamanhoMl":self.tamanhoMl
        }