# lista = [0,0,0,0,0]
# nova_lista = []
# print(float(5//2))

# for i in range(5):
#    lista[i] = int(input(f"Digite o {i + 1} número:  "))
#    if lista[i] % 2 == 0 and lista[i] != 0 :
#       nova_lista.append(lista[i])


# print(f"Números pares: {nova_lista}")

numeros = []
pares = []
impares = []

for i in range(10):
    n = int(input("Digite um número: "))
    numeros.append(n)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")