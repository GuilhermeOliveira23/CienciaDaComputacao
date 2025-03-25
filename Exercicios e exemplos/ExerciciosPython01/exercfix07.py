# Obter três notas e informar a média aritmética delas
import numpy as np

notas = np.zeros(3)

for i in range(3) :
    
    notas[i] = float(input(f"Insira a sua nota do {(i +1):.0f}º semestre: \n "))

media = np.mean(notas)

print(f"Sua média é: {media:.0f}")