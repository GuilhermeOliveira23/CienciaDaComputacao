# Solicite ao usuário um número inteiro e,
# utilizando a estrutura while, determine quantos dígitos esse número tem.
try:
    n = int(input("Digite um numero inteiro: \n"))
except:
    print("Número tem que ser inteiro")


n = str(n)
print(f"Quantidade de caracteres: {len(n)}")