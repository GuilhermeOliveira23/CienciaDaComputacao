# Função para verificar se um número é primo
def eh_primo(numero):
    # Números menores ou iguais a 1 não são primos
    if numero <= 1:
        return False
    
    # Verifica divisão por todos os números de 2 até a metade do número
    for divisor in range(2, numero // 2 + 1):
        # Se encontrar algum divisor, não é primo
        if numero % divisor == 0:
            return False
    
    # Se não encontrou nenhum divisor, é primo
    return True

# Programa principal
print("Verificador de Números Primos")

# Pede o número ao usuário
try:
    num = int(input("Digite um número inteiro: "))
    
    # Verifica se é primo e mostra o resultado
    if eh_primo(num):
        print(f"O número {num} é primo!")
    else:
        print(f"O número {num} não é primo.")
        
except ValueError:
    print("Por favor, digite apenas números inteiros.")