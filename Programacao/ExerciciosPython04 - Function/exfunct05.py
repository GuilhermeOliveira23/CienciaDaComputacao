# Escreva uma função que recebe dois números como parâmetros e
# retorna o máximo divisor comum (MDC) entre eles.
mdc = []
def calculo_mdc(n1,n2):
# Encontrando o MDC
    for x in range(2,max(n1,n2)):
        
         while n1 // x != 0 and n1 % x == 0 or n2 // x != 0 and n2 % x == 0:
                # Pega os MDCs
                   if n1 % x == 0 and n2 % x == 0:
                         mdc.append(x)
                         n1 //= x
                         n2 //= x
                        #  Divide os individuais se forem divisiveis
                   if n1 // x != 0 and n2 % x != 0:
                    n1 //= x 
                   if n2 // x != 0 and n1 % x != 0:
                    n2 //= x
    # Cálculo do MDC encontrado
    resultado = 1
    for x,y in enumerate(mdc):
        resultado *= y

    return(resultado)    

    

print(calculo_mdc(16,16))


