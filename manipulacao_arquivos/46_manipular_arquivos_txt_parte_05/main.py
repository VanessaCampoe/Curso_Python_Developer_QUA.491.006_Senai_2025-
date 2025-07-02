try:
    arquivo = input("informe  o nome do arquivo (sem extensão) :").strip().lower()
    with open(f"{arquivo}.txt", "r", encoding="utf-8") as f:  # o f se refere  as f refere-se ao nome do arquivo que o usuario digitou, o .txt é a extensão do arquivo, o encoding="utf-8" é para ler o arquivo em português brasileiro, se não colocar isso pode dar erro de leitura, pois o python não sabe como ler os caracteres especiais do português brasileiro
        # o with open(f"{arquivo}.txt", "r", encoding="utf-8
        # aqui ele vai abrir o arquivo em modo leitura  // o r de read significa leitura, o w de write significa escrita
        
        texto = f.read() # o f.read( ) significa que ele vai ler todos os dados do arquivo e armazenar na variavel texto, mas o f.read() pode receber um parametro que é o numero de caracteres que ele vai ler, por exemplo f.read(10) vai ler os 10 primeiros caracteres do arquivo, f faz referencia 
        print(f"texto gravado : \n{texto}")
        
        
        novo_texto = input("Digite o novo texto para substituir o arquivo: ")
        nova_gravacao = f"{texto}\n{novo_texto}"
        
        
        
        with open(f"{arquivo}.txt", "w", encoding="utf-8") as f:
            f.write(nova_gravacao)
            print("Gravação realizada com sucesso!")


        with open(f"{arquivo}.txt", "r", encoding="utf-8") as f:
            texto_final = f.read()
            
        print(f"Texto final :{nova_gravacao}")
except Exception as e:
    print(f"Não foi possível ler o arquivo. {e}") 