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

nome_pesquisa = input("Informe o nome a ser pesquisado: ").title().strip()
if nome_pesquisa in lista:
    print("Nome encontrado na lista.")
else:
    print("Nome não encontrado na lista.")
nome_alterar = input("Informe o nome a ser alterado: ").title().strip()
if nome_alterar in lista:
    novo_nome = input("Informe o novo nome: ").title().strip()
    lista[lista.index(nome_alterar)] = novo_nome
    print("Nome alterado com sucesso.")
    
# mostar lista com nomes inclusos
print("Lista de nomes atualizada:", lista)