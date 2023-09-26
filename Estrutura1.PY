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

def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

fatorialCalculado = fatorial(3)
print(fatorialCalculado)


# 7 - Sequencia de Fibonacci

def sequencia_fibonacci(n):
    sequencia = [0, 1]
    for i in range(2, n + 1):
        proximo_numero = sequencia[i - 1] + sequencia[i - 2]
        
        if proximo_numero <= n:
            sequencia.append(proximo_numero)
        else:
            break
    return sequencia

valor_maximo = int(input("Digite o valor máximo para a sequência de Fibonacci: "))
sequencia_fib = sequencia_fibonacci(valor_maximo)
print("Sequência de Fibonacci até", valor_maximo, ":", sequencia_fib)

# 8. Primo ou nao

numero = int(input("Digite um número: "))

def teste(numero):
    contador = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1
        
    if contador == 2:
        return 'primo'
    else:
        return 'nao'

resultado = teste(numero)
print(resultado)

# 9. Nome e leia a letra A

lista_nomes = ["Arthur", "Neymar", "Teste", "Alguma coisa", "aaqeq", "dajksdad"]

nomes_com_a = list(filter(lambda nome: nome.lower().startswith('a'), lista_nomes))

print("Nomes que começam com 'A':")
for nome in nomes_com_a:
    print(nome)

# 10. Pedra, papel, tesoura.

import random

opcoes = ["Pedra", "Papel", "Tesoura"]

escolha_usuario = input("Escolha Pedra, Papel ou Tesoura: ").capitalize()
escolha_computador = random.choice(opcoes)

print(f"Computador escolheu: {escolha_computador}")

if (escolha_usuario, escolha_computador) in [("Pedra", "Tesoura"), ("Tesoura", "Papel"), ("Papel", "Pedra")]:
    resultado = "Usuário venceu!"
elif escolha_usuario == escolha_computador:
    resultado = "Empate!"
else:
    resultado = "Computador venceu!"

print(resultado)