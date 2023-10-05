# 6 - Produto, nome, preço, qualidade.

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade

# Exemplo de uso da classe
produto1 = Produto("Vestido", 20.0, 3)
produto2 = Produto("Body", 30.0, 2)

total_produto1 = produto1.calcular_total()
total_produto2 = produto2.calcular_total()

print(f"Total do {produto1.nome}: R${total_produto1:.2f}")
print(f"Total do {produto2.nome}: R${total_produto2:.2f}")