# 10 - Funcionario, nome, salario e cargo

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual_aumento):
        if percentual_aumento > 0:
            aumento = (percentual_aumento / 100) * self.salario
            self.salario += aumento
            print(f"O salário de {self.nome} houve aumentado de {percentual_aumento}% para R${self.salario:.2f}")
        else:
            print("O percentual de aumento deve ser maior que zero.")


funcionario1 = Funcionario("Diego", 1300, "Caixa")
funcionario2 = Funcionario("Larissa", 5000, "Chefe")

funcionario1.aumentar_salario(10)
funcionario2.aumentar_salario(5)