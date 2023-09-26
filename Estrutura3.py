#1.  5 notas, aprovado ou reprovado

soma_notas =0

for i in range(1, 6):
    nota = float(input(f"Digite a {i} nota: "))
    soma_notas += nota  

media = soma_notas / 5

if media >= 7:
    print(f"Média: {media:.2f}")
    print("Aprovado")
else:
    print(f"Média: {media:.2f}")
    print("Reprovado")

# 2. fatorial por usuario

def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
        print(fatorial)
    return fatorial

 
numero = int(input("Digite um número inteiro positivo: "))
    
resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")

# 3. Palindromo 

frase = str.upper(input('Digite uma frase: ')).strip()
fraseLimpa = str.replace(frase, ' ','')
if fraseLimpa == fraseLimpa[::-1]:
    print('é palíndromo')
else:
    print('não é palíndromo')

# 4. inteiro positivo + soma

numero = int(input("Digite um número inteiro: "))
numeroString = str(numero)  
digitos = []

for digito_char in numeroString:
    digito = int(digito_char)
    digitos.append(digito)

soma = sum(digitos)

print("soma dos dígitos é:", soma)

# 5. Primo ou nao

num = int(input("Digite um número: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "não é primo")
            break
    else:
        print(num, "é primo")
else:
    print(num, "não é primo")

# 6. String de vogais

def conta_vogais(string):
    nome = string.lower()
    result = 0
    vogais = 'aeiou'
    for i in vogais:
        result += nome.count(i)
    return result

solicitado = input('informe a string ')
print(conta_vogais(solicitado))

# 7. Imc

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("seu peso: "))
altura = float(input("sua altura: "))

resultado = calcular_imc(peso, altura)

print(f"Seu IMC é {resultado:.1f}")

# 8. Ceusios Fahrenheit 

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

opcao = int(input("digite 1 para  converter de Celsius para Fahrenheit e 2 para o contrario"))

if opcao == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    resultado = celsius_para_fahrenheit(celsius)
    print(f"{celsius} graus Celsius equivalem a {resultado:.2f} graus Fahrenheit.")
else:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    resultado = fahrenheit_para_celsius(fahrenheit)
    print(f"{fahrenheit} graus Fahrenheit equivalem a {resultado:.2f} graus Celsius.")
 
# 9. Calculadora

def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "nao pode ser dividido por zero"
    return x / y

print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = int(input("Digite o número da operação desejada: "))

if opcao in [1, 2, 3, 4]:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        resultado = somar(numero1, numero2)
        operacao = "adição"
    elif opcao == 2:
        resultado = subtrair(numero1, numero2)
        operacao = "subtração"
    elif opcao == 3:
        resultado = multiplicar(numero1, numero2)
        operacao = "multiplicação"
    else:
        resultado = dividir(numero1, numero2)
        operacao = "divisão"

    print(f"O resultado da {operacao} é: {resultado}")
else:
    print("Opção inválida. Por favor, escolha uma operação de 1 a 4.")

# 10. Fibonacci 

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

