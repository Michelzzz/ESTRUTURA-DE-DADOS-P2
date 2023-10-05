# 4 - Conta bancaria 

class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para o saque.")
        else:
            print("O valor do saque deve ser maior que zero.")

    def consultar_saldo(self):
        return self.saldo


minha_conta = ContaBancaria("Jessica")
print(f"Saldo inicial da conta de {minha_conta.titular}: R${minha_conta.consultar_saldo():.2f}")

minha_conta.depositar(1000.0)
print(f"Saldo após o depósito: R${minha_conta.consultar_saldo():.2f}")

minha_conta.sacar(500.0)
print(f"Saldo após o saque: R${minha_conta.consultar_saldo():.2f}")
