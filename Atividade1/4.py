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