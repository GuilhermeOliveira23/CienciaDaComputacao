# Leia as notas de um aluno até que o valor da nota seja negativo.
#  Após a leitura, calcule a média das notas positivas e informe se o aluno foi aprovado (média >= 7),
#  reprovado (média < 4) ou de recuperação (média entre 4 e 7).

import numpy as np
array = np.zeros(3)
for i in range(3):
    
    array[i] = int(input("Digite a sua nota\n"))


media = np.mean(array)
if media < 4:
   print(f"Aluno foi reprovado")
elif media >= 7:
   print(f"Aluno foi aprovado")
else:
   print(f"Aluno está de recuperação")
