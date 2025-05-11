# 4. Faça um programa que simule um baralho
# e escolha cartas aleatórias para iniciar
# uma partida de Poker Texas Hold’em


import random
baralho = [1,2,3,4,5,6,7,8,9,10,11,12,13]
n = random.randrange(1,14)

print(f"Sua carta tem o valor de: {n}")
baralho.remove(n)
print(baralho)