import math as m

# Código para calcular juros compostos
valor_inicial = float(input("Digite o valor inicial: "))


periodo = 12  # Período de 12 meses

# Calcula o valor final com juros compostos
valor_final = valor_inicial * m.pow(1 + 0.018 , periodo)

# Exibe o resultado
print(f"Valor final após {periodo} meses: R$ {valor_final:.2f}")