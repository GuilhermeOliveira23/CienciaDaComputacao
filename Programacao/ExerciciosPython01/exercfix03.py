from datetime import datetime as date

def dataNascimentoCalculo():
    
    try:
       
        dataNascimento = date.strptime(input("Digite a sua data de nascimento (DD/MM/YY)\n"), "%d/%m/%Y")
        idade = date.today()-dataNascimento
        
        return idade
    except ValueError:

        print("Formato invalido")
    

print(f"\nVocê nasceu há exatamente: {dataNascimentoCalculo().days} dias")
