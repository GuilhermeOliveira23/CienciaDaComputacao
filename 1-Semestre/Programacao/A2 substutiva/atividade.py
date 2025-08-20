def porcentagem(participantes):
    resultado = livros[vencedor] / participantes  * 100
    return resultado


livros = {"Dom Casmurro": 0, "Vidas Secas": 0, "Capitães da Areia": 0, "O Cortiço": 0, "Iracema": 0, "Memórias Póstumas de Brás Cubas": 0, "Senhora": 0, "Macunaíma": 0, "A Hora da Estrela": 0, "O Quinze": 0}

participantes = 0
votos = True
empate = False


print(f"Escolha o livro em que deseja votar(digitando o seu número): \n|1-Dom Casmurro, 2-Vidas Secas, 3-Capitães da Areia, 4-O Cortiço, 5-Iracema, 6-Memórias Póstumas de Brás Cubas, 7-Senhora, 8-Macunaíma, 9-A Hora da Estrela, 10-O Quinze|\nDigite 999 para sair do programa")
while votos:
    escolha = input("Digite o número do livro correspondente: ")
    if escolha == "1":
        participantes += 1
        livros["Dom Casmurro"] += 1
    elif escolha == "2":
        participantes += 1
        livros["Vidas Secas"] += 1
    elif escolha == "3":
        participantes += 1
        livros["Capitães da Areia"] += 1
    elif escolha == "4":
        participantes += 1
        livros["O Cortiço"] += 1
    elif escolha == "5":
        participantes += 1
        livros["Iracema"] += 1
    elif escolha == "6":
        participantes += 1
        livros["Memórias Póstumas de Brás Cubas"] += 1
    elif escolha == "7":
        participantes += 1
        livros["Senhora"] += 1
    elif escolha == "8":
        participantes += 1
        livros["Macunaíma"] += 1
    elif escolha == "9":
        participantes += 1
        livros["A Hora da Estrela"] += 1
    elif escolha == "10":
        participantes += 1
        livros["O Quinze"] += 1
    elif escolha == "999":
        votos = False
    else: 
        print("Erro: Texto recebido não é número ou não está na lista de livros. Tente novamente!!!")
# List comprehension
chaves_max = [chave for chave, valor in livros.items() if valor == max(livros.values())]
vencedor = max(livros, key=livros.get)
print("Votos:")
print(f"1-Dom Casmurro: {livros['Dom Casmurro']}, 2-Vidas Secas: {livros['Vidas Secas']}, 3-Capitães da Areia: {livros['Capitães da Areia']}, 4-O Cortiço: {livros['O Cortiço']},\n 5-Iracema: {livros['Iracema']}, 6-Memórias Póstumas de Brás Cubas: {livros['Memórias Póstumas de Brás Cubas']}, 7-Senhora: {livros['Senhora']}, 8-Macunaíma: {livros['Macunaíma']},\n 9-A Hora da Estrela: {livros['A Hora da Estrela']}, 10-O Quinze: {livros['O Quinze']}")
if len(chaves_max) < 2:
    
    print(f"{vencedor} é o candidato vencedor da votação com {porcentagem(participantes):.0f}% dos votos!!!")
else:

    print(f"Os vencedores foram:")
    for i in chaves_max:
        print(i)

    print(f"Com {porcentagem(participantes):.0f}% dos votos!!!")
    