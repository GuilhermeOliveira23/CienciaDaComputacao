import numpy as np

matriz = np.zeros((10,10))

for i in range(10):
    matriz[i, i] = 1

print(matriz)