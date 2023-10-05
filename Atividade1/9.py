# 9. Nome e leia a letra A

lista_nomes = ["Arthur", "Neymar", "Teste", "Alguma coisa", "aaqeq", "dajksdad"]

nomes_com_a = list(filter(lambda nome: nome.lower().startswith('a'), lista_nomes))

print("Nomes que começam com 'A':")
for nome in nomes_com_a:
    print(nome)