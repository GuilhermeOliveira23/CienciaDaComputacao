# Escreva uma função que recebe um número inteiro como parâmetro e
# retorna uma lista contendo todos os números primos menores ou iguais ao número fornecido.
def is_prime(n):
    if n <= 1:
         return False
    if n == 2:
         return True
    if n % 2 == 0:
         return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
         return False
    return True



def primos_ate(numero):
    primos = []
    for i in range(2, numero + 1):
        if is_prime(i):
         primos.append(i)
    return primos

num = int(input("Número:  "))
print(primos_ate(num))
