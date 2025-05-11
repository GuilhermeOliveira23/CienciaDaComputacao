import math as math
# Qual é a raiz quadrada do maior número entre 2, 5 e 8 
# elevado ao menor número entre 3, 7 e o dobro destes?

maior = max(2,5,8)
menor = min(3, 7, 3 * 2, 7 * 2)
exponencial = pow(maior,menor)
raizQuadrada = math.sqrt(exponencial)

print(f"|Resultado meio gay: {raizQuadrada}")

# OUUUUU
resultado = math.sqrt(pow(max(2,5,8),min(3,7,3*2,7*2)))
print(resultado)