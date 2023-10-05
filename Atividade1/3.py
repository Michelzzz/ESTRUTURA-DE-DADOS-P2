# 3 - todos os numeros pares de 0 ate ele

numeros_pares = int(input("Digite um numero: "))

print("Numeros pares de 0 ate", numeros_pares,":")
for i in range (0, numeros_pares + 1, 2):
    print(i)