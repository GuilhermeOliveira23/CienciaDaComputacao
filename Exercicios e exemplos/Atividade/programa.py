# Os alunos devem votar no melhor professor.
# o programa deve mostrar  um menu com nomes:
# minerva, Severus, Remus, Horace, Gilderoy.
# Cada voto será digitado como texto com o nome do professor.
# a votação encerra com a palavra "fim".
# O programa deve aceitar variações de maiusculas ou minúsculas
# ou pequenos erros de grafia e tratar isso adequadamente.
# após o encerramento, exiba:
# Total de cada voto de cada professor
# Nomes dos vencedores
# Porcentagem do vencedor
def encontrar_vencedor(votos1, votos2, votos3, votos4, votos5):
    # Verifica o maior valor entre todos
    maior = votos1
    vencedor = "Minerva"
    
    if votos2 > maior:
        maior = votos2
        vencedor = "Severus"
    if votos3 > maior:
        maior = votos3
        vencedor = "Remus"
    if votos4 > maior:
        maior = votos4
        vencedor = "Horace"
    if votos5 > maior:
        maior = votos5
        vencedor = "Gilderoy"
    
    # Verifica empate
    empate = (
        (votos1 == maior and (votos2 == maior or votos3 == maior or votos4 == maior or votos5 == maior)) or
        (votos2 == maior and (votos3 == maior or votos4 == maior or votos5 == maior)) or
        (votos3 == maior and (votos4 == maior or votos5 == maior)) or
        (votos4 == maior and votos5 == maior)
        )
    
    if empate:

        return "Houve um empate!"
    else:

        return vencedor


def Porcentagem(votos, alunos):
    resultado = (votos / alunos) * 100
    return resultado

print(f"Escolha o professor que deseja votar: \n|Minerva Severus Remus Horace Gilderoy|")

Minerva = 0
Severus = 0
Remus = 0 
Horace = 0
Gilderoy = 0

alunos = 4
for x in range(alunos):
    professor = input("Digite o nome do professor:")
    if professor == "Minerva" or professor == "minerva" or professor == "MINERVA":
        Minerva +=1
       
    elif professor == "Severus" or professor == "SEVERUS" or professor == "severus":
        Severus += 1
       
    elif professor == "Remus" or professor == "REMUS" or professor == "remus":
        Remus += 1
       
    elif professor == "Horace" or professor == "HORACE" or professor == "horace":
        Horace += 1
       
    elif professor == "Gilderoy" or professor == "GILDEROY" or professor == "gilderoy":
        Gilderoy += 1
       
    else:
        print("Digite o nome corretamente!!")
print(f"Votos Minerva: {Minerva}, Votos Severus: {Severus}, Votos Remus: {Remus}, Votos Horace: {Horace}, Votos Gilderoy: {Gilderoy}")
votos = max(Minerva,Severus,Remus,Horace,Gilderoy)
vencedor = encontrar_vencedor(Minerva, Severus, Remus, Horace, Gilderoy)
print(f"Vencedor: {vencedor} Com a porcentagem de votos de {Porcentagem(votos,alunos):.0f}%")
