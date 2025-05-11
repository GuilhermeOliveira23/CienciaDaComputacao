# Escreva uma função que recebe uma
# lista de números como parâmetro
# e retorna a média desses números.
import numpy as np
array = np.zeros(2)
print(array)

def Media(lista):
    for i in range(2):
        lista[i]=int(input("Me fale um número: "))
    return np.mean(lista)


print(Media(array))