numero = int(input("Informe um número primo:\n"))
primo = 0

for i in range(1, int(numero/2)+1):
    if numero % i != 0:
        print(i)
        if primo == 0:
            
            primo += 1
            print("Numero é primo")
        else:
            break
  
if primo == 0:
    print("Número não é primo")