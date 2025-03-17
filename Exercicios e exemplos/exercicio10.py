texto = str(input("Digite um texto: ").replace(" ", ""))
vogais ="aeiouAEIOU"
freq_vogais = {}
for vogal in vogais:
    freq_vogais[vogal] = texto.count(vogal)

for vogal, ocorrencias in freq_vogais.items():
    freq_vogais[vogal] = ocorrencias / len(texto)

print("Frequencia relativa das vogais: ")
for vogal, freq in freq_vogais.items():
    
    print(f"{vogal}: {freq:.2%}")