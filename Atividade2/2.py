# 2 - Livro, autor e titulo.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"


meu_livro = Livro("Diário de uma paixão", "Nicholas Sparks")
informacoes = meu_livro.detalhes()
print(informacoes)