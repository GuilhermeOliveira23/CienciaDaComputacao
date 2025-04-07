# Implemente um jogo de adivinhação onde o usuário precisa adivinhar um número aleatório entre 1 e 500.
# O programa deve dar dicas se o número escolhido for maior ou menor do que o palpite,
#  até que o usuário acerte.
import random as rng
n = rng.randrange(0,500)
tentativas = 4
print(n)
while tentativas != 0:
    tentativas -=1
    palpite = int(input("Advinhe o número:\n"))
    if palpite > n:
        print("Seu palpite é maior que o número")
    elif palpite == n:
        print("Parabéns você acertou!!!")
        break
    else:
        print("Seu palpite é menor que o número")
if palpite != n and tentativas == 0:
    print(f"O número era {n}")