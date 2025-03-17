#criar uma tabela de multiplicaçao do 1 ate o 10
print("  |  1  2  3  4  5  6  7  8  9 10")
for i in range (1,11):
    # print( f"Tabuada do numero {i}:")
    print(f"\n{i} | ", end="")

        
    for j in range(1,11):
 
        resultado = i * j        
        print(f"{resultado:2}", end=" ")
5
print()