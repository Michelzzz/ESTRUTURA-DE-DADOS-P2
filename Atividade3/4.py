# 4. inteiro positivo + soma

numero = int(input("Digite um número inteiro: "))
numeroString = str(numero)  
digitos = []

for digito_char in numeroString:
    digito = int(digito_char)
    digitos.append(digito)

soma = sum(digitos)

print("soma dos dígitos é:", soma)