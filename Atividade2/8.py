# 8 - Aluno, nome notas.

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        if len(self.notas) > 0:
            return sum(self.notas) / len(self.notas)
        else:
            return 0  # Retorna 0 se não houver notas


notas_aluno1 = [9.4, 6.6, 9.2, 8.6]
aluno1 = Aluno("Douglas", notas_aluno1)

notas_aluno2 = [10, 5.5, 9.5, 7.0]
aluno2 = Aluno("Jossicleide", notas_aluno2)

media_aluno1 = aluno1.calcular_media()
media_aluno2 = aluno2.calcular_media()

print(f"A média das notas de {aluno1.nome} é {media_aluno1:.2f}")
print(f"A média das notas de {aluno2.nome} é {media_aluno2:.2f}")