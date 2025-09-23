# importçaõ
import os 
# entrada  de dados 
while True:
    try:
        aquivo  = input("informe  o nome do arquivo :").strip().lower()
        
        # abre o arquivo 
        with open(f"{aquivo}.txt", "r", encoding="utf-8") as f:  # r de read modo leitura  # encoding o tipo de leitura do pt br  fazer um eyras   chamdo de f 
            arquivo_aberto = f.read()  # ler o conteudo do arquivo
            # saida dos dados
            os.system("cls" if os.name == "nt" else "clear")
            # mostra o conteudo do arquivo
            print(arquivo_aberto)
        
        
        while True:
            # pergunta se o usuario quer continuar
            pressionar = input("Deseja abrir outro arquivo ? (s/n): ").strip().lower()
            if pressionar == "s" or pressionar == "sim":
                break
            else:
                print("Opção invalida.")
                continue
        match pressionar :
            case "s" :
                continue
            case "n" :
                break

    except Exception as e :
        print(f" Não foi possivel ler o arquivo . {e} ")
        continue