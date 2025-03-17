# Obter o valor de um empréstimo e informar quanto deve ser pago considerando que será pago em 12 meses com juros simples de 0,8% a.m.
valor = float(input("Digite o valor do emprestimo: \n"))

valorFinal = lambda valor : valor + valor * 0.018 * 12

print(f"Valor dos juros do empréstimos: {valorFinal(valor):.2f}")