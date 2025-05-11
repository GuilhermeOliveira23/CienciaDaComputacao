# Escreva uma função que recebe um número como parâmetro e retorna se o número é primo ou não

def numero_primo(numero):

    if numero <= 1:
        return False
    
    for divisor in range(2,numero // 2 + 1):
        
        if numero % divisor == 0 :
            return False
    
    return True

print("Verificador de Números Primos")

try:
    num = int(input("Digite um número primo: "))
    if numero_primo(num) :
        print(f"O número {num} é primo!!!")
    else:
        print(f"O número {num} não é primo!!!")

except ValueError:
    print("Por favor, digite apenas números inteiros")