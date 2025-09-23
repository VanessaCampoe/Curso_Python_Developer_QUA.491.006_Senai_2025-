# lista de cidaes 
cidades = [
    "brasilia"
    "Sao Paulo",
    "Rio de Janeiro",
    "Teresina",
    "Belo Horizonte",
    "Palmas",
    
 ]
for i in range(len(cidades)):
    print(f"Indice{i}: {cidades[i]}.")
    
    # usuario informa um nome da nova cidade que deseja inserir 
try:
    nova_cidade = input("Informe o nome da nova cidade: ").title().strip()
    i = int(input("Informe o indice onde deseja inserir a nova cidade: "))    #aqui e quando penso em jogar meu tratamento de exeção

    if i >= 0 and i <= len(cidades):
        cidades.insert(i,nova_cidade)
        print("Cidade inserida com sucesso")
        
    else:            
        print("Indice invalido.")
     
except Exception as e:
    print(f"Não foi possivel  inserir item na lista. {e}.")
finally:
   #re-exibe a lista de cidades
   for i in range(len(cidades)):
       print(f"Indice {i}: {cidades[i]}.")    
     