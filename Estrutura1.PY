import random

# 1 - media de 3 numeros inseridos pelo usuario

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))
total = (num1 + num2 + num3) /3

print("A media dos numeros é de: ", {total})


# 2 - Se o numero inserido é impar ou par

numero1 = int(input("Insira um numero: "))

if numero1 % 2 == 0:
    print("O numero é par")
else:
    print("O numero é impar")


# 3 - todos os numeros pares de 0 ate ele

numeros_pares = int(input("Digite um numero: "))

print("Numeros pares de 0 ate", numeros_pares,":")
for i in range (0, numeros_pares + 1, 2):
    print(i)


# 4 - Lista e ler o maior e menor numero

lista_numeros = []
    
elementos_da_lista = int(input("Digite o número de elementos na lista: "))
    
for i in range(elementos_da_lista):
        numero = float(input(f"Digite o {i+1}º número: "))
        lista_numeros.append(numero)

if lista_numeros:
        maior = max(lista_numeros)
        menor = min(lista_numeros)
        
        print(f"O maior número na lista é: {maior}")
        print(f"O menor número na lista é: {menor}")
else:
        print("A lista está vazia.")


# 5 - Lista de numeros e media dos numeros pares

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

# 6 - Numero inteiro positivo do usuario + fatorial



# 7 - Sequencia de Fibonacci

