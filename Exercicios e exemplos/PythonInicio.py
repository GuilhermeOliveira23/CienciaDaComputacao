#Contra barra n (\n) quebra de linha
n = int(input("Digite um número de 1 a 10 apenas:\n"))

if n == 1:
 fatorial = 1
elif n >= 10 or n <= 1:
 print("Apenas numeros de 1 a 10 podem ser calculados!!")
else:
    fatorial = n
    n2 = n
    while n2 > 1:
     n2 -= 1
     fatorial *= n2

print(f"O fatorial de {n} é {fatorial}!")