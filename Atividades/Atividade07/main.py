# crie um porgraam que faça a seguinte opreção ,
# cadastre um novo nome na lista
# lsita o nome na lista 
# pesquise por um nome na lista 
# Altere um nome na lista .......
# Exclua o nome na lista 
# Sair do programa
# A lista deve começar vazia . Exemplo : lista = []
#
lista = []
# aqui vamos cadastrar uma lista vazia 
# aqui a configurção da lista 
nome = input("Informe o nome: ").title().strip()
lista.append(nome)
print("Lista de nomes:", lista)
#incluir varios nomes na lista

while True:
    nome = input("Informe outro nome (ou digite 'sair' para encerrar): ").title().strip()
    if nome.lower() == 'sair':
        break
    lista.append(nome)
    print("Lista de nomes:", lista)
    # mostrar todos os nomes incluidos na lista 
    
# aqui vamos pesquisar o nome na lista 

nome_pesquisa = input("Informe o nome a ser pesquisado: ").title().strip()
if nome_pesquisa in lista:
    print("Nome encontrado na lista.")
else:
    print("Nome não encontrado na lista.")
    
    # aqui devo voltar para perguntar quando o novo nome a ser encontrado pq pulou dif=reto  para nome a ser alterado  
    
    # aqui vamos alterar o nome da lista   
    
nome_alterar = input("Informe o nome a ser alterado: ").title().strip()
if nome_alterar in lista:
    novo_nome = input("Informe o novo nome: ").title().strip()
    lista[lista.index(nome_alterar)] = novo_nome
    print("Nome alterado com sucesso.")
    
# mostar lista com nomes inclusos
print("Lista de nomes atualizada:", lista)

# praticamente o que estamos fazendo aqui e um crud , um crude significa create, read,update e delete 


# excluir nome da lista 
nome_excluir = input("Informe o nome a ser excluído: ").title().strip()
if nome_excluir in lista:
    lista.remove(nome_excluir)
    print("Nome excluído com sucesso.")
    
# mostar lista com nomes inclusos
print("Lista de nomes atualizada:", lista)
