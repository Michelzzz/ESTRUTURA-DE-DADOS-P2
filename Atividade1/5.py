# 5 - Lista de numeros e media dos numeros pares

import random
tamanho_lista = int(input("Digite o tamanho da lista: "))
limite_superior = int(input("Digite o limite superior para os números aleatórios: "))
    
lista_numeros1 = [random.randint(1, limite_superior) for _ in range(tamanho_lista)]
    
numeros_pares = [numero for numero in lista_numeros1 if numero % 2 == 0]
    
if numeros_pares:

    media = sum(numeros_pares) / len(numeros_pares)
    print(f"A lista de números aleatórios é: {lista_numeros1}")
    print(f"A média dos números pares é: {media}")
else:

    print("Não há números pares na lista.")