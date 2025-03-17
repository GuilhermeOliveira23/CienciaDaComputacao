n1 = int(input("Digite um numero:\n"))

# Obter um valor e informar qual é a menor quantidade
# possível de notas de 2, 5, 10, 20, 50,100 e 200 na qual o valor pode ser decomposto
notas200 = n1 // 200
resto = n1 % 200

notas100 = resto // 100
resto %= 100

notas50 = resto//50
resto %=50

notas20= resto//20
resto %= 20

notas10 = resto //10
resto %= 10

 

if resto % 2 == 0:
    notas2 = resto//2
    notas5 = 0
else:
    notas5 = resto // 5
    resto %= 5

    notas2 = resto // 2


print(f"Notas de 200: {notas200}")
print(f"Notas de 100: {notas100}")
print(f"Notas de 50: {notas50}")
print(f"Notas de 20: {notas20}")
print(f"Notas de 10: {notas10}")
print(f"Notas de 5: {notas5}")
print(f"Notas de 2: {notas2}")

