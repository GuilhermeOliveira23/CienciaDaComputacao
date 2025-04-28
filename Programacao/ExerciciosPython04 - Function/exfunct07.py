# Escreva uma função que recebe uma lista como parâmetro e 
# retorna uma nova lista com os elementos da lista original em ordem inversa.

# Método usando classes
class MinhaClasse:
    lista = [1,2,3,4,5,6,7,8,9,10]
    
    def lista_reverse(lista):
        
        lista = MinhaClasse.lista.copy()
        lista.reverse()
        return lista
    
print(MinhaClasse.lista_reverse(MinhaClasse.lista))

# Método mais eficiente
def lista_inversa(lista):
    nova_lista = lista[::-1]
    return  nova_lista
print(lista_inversa(MinhaClasse.lista))