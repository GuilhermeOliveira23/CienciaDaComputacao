# Faça um programa gerador de senhas,
# que crie alguma com a quantidade desejada de caracteres,
# com uma combinação de maiúsculas, minúsculas e algarismos
# import secrets
# n= secrets.token_bytes(10)
# print(n)

import random
lower = "abcdefghiklmnopqrstuvyxz"
upper = lower.upper()
numbers ="0123456789"
symbols = "!@#$%&*().^"
string = lower + upper + numbers + symbols
length = 16
password = "".join(random.sample(string,length))
print("Sua senha nova é: "+ password)