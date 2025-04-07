# Solicite ao usuário dois números inteiros, a base e o expoente,
# e calcule a potência (base^expoente) utilizando a estrutura while,
# sem utilizar o operador ** ou a função pow().
n1 = int(input("Digite a base: "))
n2 = int(input("Digite o expoente: "))
while n2 != 0:
    n2 -= 1
    res =(n1 * n1)
print(f"Balkan rage tá ai a resposta: {res}")