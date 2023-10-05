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