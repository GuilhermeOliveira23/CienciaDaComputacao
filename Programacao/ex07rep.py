# Solicite ao usuário um número inteiro e,
# utilizando a estrutura while,
# calcule a soma dos seus dígitos 
# (por exemplo, para o número 123, a soma seria 1 + 2 + 3 = 6).]
# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Inicializa a variável para armazenar a soma
soma_digitos = 0

# Converte o número para positivo para facilitar o cálculo
numero = abs(numero)

# Calcula a soma dos dígitos usando while
while numero > 0:
    # Obtém o último dígito
    digito = numero % 10
    # Adiciona o dígito à soma
    soma_digitos += digito
    # Remove o último dígito do número
    numero = numero // 10

# Exibe o resultado
print(f"A soma dos dígitos é: {soma_digitos}")