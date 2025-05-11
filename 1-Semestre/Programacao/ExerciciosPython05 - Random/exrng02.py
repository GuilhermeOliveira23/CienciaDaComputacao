# 2. Faça um programa no qual o computador escolhe um número inteiro
# de 1 a 100 e pede para o usuário adivinhar.
# A cada tentativa o usuário deve ser informado
# se o número que ele tentou é o correto
# ou se é maior ou menor do que o correto
import random as rng
n_sorteado = rng.randrange(1, 101)
print (n_sorteado)
n = int(input("Digite um número entre 1 e 100"))
if n < n_sorteado:
    print("Número é menor do que o sorteado")
if n > n_sorteado:
    print("Numero é maior do que o sorteado")
if n == n_sorteado:
    print("Você acertou!!!")
