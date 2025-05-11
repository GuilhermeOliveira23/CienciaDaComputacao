# Escreva código recursivo para calcular MDC
def calculo_mdc_finalboss(a,b):
    """
    Calcula o Máximo Divisor Comum (MDC) entre dois números inteiros a e b
    usando o algoritmo de Euclides de forma recursiva.
    """
    # Caso base: quando b é zero, o MDC é a
    if b == 0:
        return a
    # Passo recursivo: mdc(a, b) = mdc(b, a % b)
    else:
        return calculo_mdc_finalboss(b, a % b)

# Exemplo de uso:
num1 = 48
num2 = 18
resultado = calculo_mdc_finalboss(num1, num2)
print(f"O MDC entre {num1} e {num2} é {resultado}")