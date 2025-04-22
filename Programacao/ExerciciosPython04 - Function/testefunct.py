import time

def Fala():
        
        print("Sara ni")
        time.sleep(2)
        print("Ryouki Tenkai")

# Fala()

def fatorial(n):
  return 1 if (n == 1 or n == 0) else n * fatorial(n - 1)

# numero = 10
# resultado = fatorial(numero)
# print(f"O fatorial de {numero} é {resultado}")


def hanoi(discos, orig, dest, aux):
  if discos == 1:
    print(f"Mover disco 1 de {orig} para {dest}")
    return

  hanoi(discos - 1, orig, aux, dest)
  print(f"Mover disco {discos} de {orig} para {dest}")
  hanoi(discos - 1, aux, dest, orig)

hanoi(8, 'A', 'C', 'B')