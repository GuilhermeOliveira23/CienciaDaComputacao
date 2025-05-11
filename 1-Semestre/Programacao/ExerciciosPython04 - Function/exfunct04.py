# Escreva uma função que recebe um número inteiro como parâmetro e retorna o fatorial desse número.
 
def calculo_fatorial(n):
    for x in range(1,n):
        n *= x
    return n
       
    
fatorial = int(input("digite um número: "))

print(calculo_fatorial(fatorial))
