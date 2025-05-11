# Solicite dois números inteiros e calcule a divisão inteira e o resto da divisão.
#  Utilize o laço while para garantir que os dois números são diferentes de zero,
#  e repita a leitura até que isso seja cumprido.
n1 = 0
n2 = 0
while n1 == 0 or n2 == 0:
    n1 = int(input("Digite um numero:"))
    n2 = int(input("Digite um numero:"))
def Calculo(n1,n2):
   
   res_div =  n1 // n2 
   res_resto = n1 % n2
   print(f"Divisão inteira : {res_div}\nResto da divisão: {res_resto}")
   
Calculo(n1,n2)