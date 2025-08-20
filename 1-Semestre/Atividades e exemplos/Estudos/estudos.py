
# n1 = int(input("Digite um número inteiro:"))
# n2 = int(input("Digite um número inteiro:"))

# print(f"soma: {n1 + n2}\nsubtração: {n1 - n2} \nmultiplicação: {n1 * n2} \nresto da divisão: {n1 % n2}")


# idade = int(input("Digite a sua idade: "))

# if idade >= 16:
#     print("Pode votar")
# else:
#     print("Não pode votar")

# n = 1
# while n <= 10:
#     print(n)
#     n += 1
# numeros = [3, 4, 7, 10, 2, 11]
# for num in numeros:
#     if num % 2 == 0:
#         print(f"Número par: {num}")
#     else:
#         pass
# user = str(input("Escreva algo: "))

# arquivo = open("frases.txt", "w")
# conteudo = arquivo.write(user)
# print(user)
# arquivo.close()


# import random as rng
# from datetime import datetime

# print("Número aleatório:" + str(rng.randrange(1, 101)))

# print(f"Data de agora: {datetime.today()}")

import tkinter as tk
from tkinter import messagebox
janela = tk.Tk()
janela.title("Saudação")

def Saudar():
    nome = input.get()
    messagebox.showinfo("Saudação", f"Olá, {nome}")
    print("Saudações!")


botao = tk.Button(janela, text="Saudar", command= Saudar)
label = tk.Label(janela, text = "Digite o seu nome: ")
input = tk.Entry(janela)

label.pack()
input.pack()
botao.pack()

janela.mainloop()