# 1. Faça um programa que simule o lançamento de um e de dois dados
import random
user = input("Deseja girar o dado? [s/n]\n")
if user == "s":
    for i in range(7):
        print(random.randrange(1,7))
else:
    pass