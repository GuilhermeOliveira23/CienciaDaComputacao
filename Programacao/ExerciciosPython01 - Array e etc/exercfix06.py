# A série de Números Pentagonais é dada por 1, 5, 12, 22, 35, ... onde cada número pode ser encontrado pela equação 
# Pn =(n/2)*(3n − 1). Faça um programa que, dado “n”, calcule seu número pentagonal.
n = int(input("Digite um numero: "))

pentagonal = (n/2) * (3*n-1)

print(f"Numero pentagonal: {pentagonal:.0f}")

