# 7 - Carro, marca, modelo e ano.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"


meu_carro = Carro("Toyota", "Corolla", 2022)
informacoes_carro = meu_carro.detalhes()
print(informacoes_carro)