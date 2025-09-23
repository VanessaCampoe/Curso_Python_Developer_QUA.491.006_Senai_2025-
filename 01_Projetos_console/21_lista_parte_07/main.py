nomes = ["Maria",
         "João",
         "Ana",
         "Pedro",
         "Lucas",
         "Laura",
         "Mariana",
         "Carlos"
         ]
# exibe a lista de nomes
for i in range(len(nomes)):
    print(f"{i}: {nomes[i]}.") 
    
try:
    i = int(input("Informe a posição do índice a ser alterado: "))
    if i >= 0 and i < len(nomes):
        
        del(nomes[i])
        print(" Nome excçiido com sucesso ")   
        
        
       
    else:
        print("Índice fora do intervalo da lista.")
    
except Exception as e:
    print(f"Não foi possivel alterar o item. {e}.")
finally:
    for i in range(len(nomes)):
        print(f"{i}: {nomes[i]}.")
    
        