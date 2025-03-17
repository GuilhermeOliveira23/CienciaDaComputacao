# x = range(3, 10, 3)
# for n in x:
#   print(n)

# for i in range(10, 0, -1):
#   print(i)
#   # Delay artificial com for, fazendo o código iterar 5 milhões de vezes, atrasando a resposta entre os prints
#   for _ in range(5000000):
#     pass
# else:
#   print("Fogo!!!")

# frutas = ["maça", "pera", "melancia"]
# caracteristica = ["verde", "madura", "saborosa"]
# for x in frutas:
#   for j in caracteristica:
#     print(x, j)

# frutas = ["maça", "pera", "melancia"]
# for x, y in enumerate(frutas):
#   print(f"fruta {x + 1} é {y}")
vetor = ["Tatooine", "Coruscant", 
  "Endor", "Hoth", "Naboo"]
# Percorre o vetor e imprime cada elemento em uma linha
for indice, elemento in enumerate(vetor, start=1):
  print(f"Item #{indice}: {elemento}")