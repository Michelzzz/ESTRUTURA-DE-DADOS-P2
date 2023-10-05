# 7. Imc

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("seu peso: "))
altura = float(input("sua altura: "))

resultado = calcular_imc(peso, altura)

print(f"Seu IMC é {resultado:.1f}")