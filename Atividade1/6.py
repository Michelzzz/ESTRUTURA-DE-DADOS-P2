# 6 - Numero inteiro positivo do usuario + fatorial

def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

fatorialCalculado = fatorial(3)
print(fatorialCalculado)