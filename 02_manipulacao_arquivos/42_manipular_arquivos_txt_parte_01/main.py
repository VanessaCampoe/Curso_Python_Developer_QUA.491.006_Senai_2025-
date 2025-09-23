# leitura  de arquivo 
with open("42_manipular_arquivos_txt_parte_01/texto.txt", "r", encoding="utf-8") as f:                        # r de ride modo leitura  # encondiding o tipo de leitura do pt br  fazer um eyras   chamdo de f 

    texto = f.read()  # ler o conteudo do arquivo
    # saida dos dados 
print(texto)  # imprimir o conteudo do arquivo
    
