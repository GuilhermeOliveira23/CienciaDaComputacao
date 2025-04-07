from datetime import date
idade = 0
while idade == 0:
    try:
    
        dataDeNascimento = int(input("Digite o ano em que nasceu:  "))
        idade = (date.today().year-dataDeNascimento)
        print(idade)
        
    except:
        print("Digite um ano valido!!!")

