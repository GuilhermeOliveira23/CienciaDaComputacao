

def fatorial():
    numero = int(input("Digite um número:\n"))
    n_fatorial = numero
    while numero != 0:   
     numero -=1
     if numero == 0:
        continue
    
     n_fatorial *= numero
    print(n_fatorial)


fatorial()