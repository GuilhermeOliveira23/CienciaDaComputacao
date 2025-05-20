def porcentagem(alunos):
    resultado = candidatos[vencedor] / alunos  * 100
    return resultado

candidatos = {"Minerva": 0, "Severus": 0,"Remus": 0, "Horace": 0, "Gilderoy": 0}

alunos = 4
teste = True
empate = False
print(f"Escolha o professor que deseja votar: \n|Minerva Severus Remus Horace Gilderoy|")


while teste <= alunos:
    professor = input("Digite o nome do professor:")
    if professor == "Minerva" or professor == "minerva" or professor == "MINERVA":
        candidatos["Minerva"] +=1
        teste += 1
       
    elif professor == "Severus" or professor == "SEVERUS" or professor == "severus":
        candidatos["Severus"] += 1
        teste += 1
       
    elif professor == "Remus" or professor == "REMUS" or professor == "remus":
        candidatos["Remus"] += 1
        teste += 1
       
    elif professor == "Horace" or professor == "HORACE" or professor == "horace":
        candidatos["Horace"] += 1
        teste += 1
       
    elif professor == "Gilderoy" or professor == "GILDEROY" or professor == "gilderoy":
        candidatos["Gilderoy"] += 1
        teste += 1
    else:
        print("Digite o nome corretamente!!")


chaves_max = [chave for chave, valor in candidatos.items() if valor == max(candidatos.values())]

if len(chaves_max) < 2:
    vencedor = max(candidatos, key=candidatos.get)
    print(f"Minerva: {candidatos['Minerva']}, Severus: {candidatos['Severus']}, Remus: {candidatos['Remus']}, Horace: {candidatos['Horace']}, Gilderoy: {candidatos['Gilderoy']}")
    print(f"{vencedor} é o candidato vencedor da votação com {porcentagem(alunos):.0f}% dos votos!!!")
else:

    print(f"A votação foi um empate entre {chaves_max[0]} e {chaves_max[1]}")