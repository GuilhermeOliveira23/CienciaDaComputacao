# Solicite ao usuário um número inteiro e imprima os termos
# da sequência de Fibonacci até que o número solicitado seja atingido ou ultrapassado.
n = int(input("Digite um numero inteiro por favor: "))
fibo = n
n1 = 0
n2 = 1
while n < fibo:
    n1 += n2
    n1 = fibo
    print(f"Sequência fibonacci {n1} {n2}")