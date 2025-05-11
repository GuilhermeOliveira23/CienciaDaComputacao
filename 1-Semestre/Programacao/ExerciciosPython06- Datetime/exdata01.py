# Faça um programa que determine o dia da semana de uma determinada data.

from datetime import datetime
dt_input = input("Data: ")
dt = datetime.strptime(dt_input, "%d/%m/%Y")
print(dt.weekday())
