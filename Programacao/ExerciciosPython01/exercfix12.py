# Obter um valor inteiro (x) e informar o resultado da expressão: y = x2 − 8x + 5

n = float(input("Digita um numero ai: "))

resultado = lambda n: 2 * n - 8 * n + 5

print(f"Resultado da expressão: {resultado(n):.0f}")