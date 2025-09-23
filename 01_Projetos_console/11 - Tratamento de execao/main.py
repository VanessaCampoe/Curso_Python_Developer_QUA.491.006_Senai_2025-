# declaração de variavel 
# tratamento de execao 
try:
    n = int(input("Informe o numero inteiro:"))
    print(f"O nuemro  inteiro informado:{n}." )
# manter essa estrutura 
#saida de dados 
except Exception as e:
    print(f"Não foi possivel exibir o numero.{e}. " )
    # print f é junto 
finally:
    print("Programa encerrado com sucesso!")