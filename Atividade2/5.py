# 5 - Pessoa, nome, idade e falar

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Olá, meu nome é {self.nome}.")

# Exemplo de uso da classe
pessoa1 = Pessoa("Benny", 30)
pessoa2 = Pessoa("Sophie", 25)

pessoa1.falar()
pessoa2.falar()