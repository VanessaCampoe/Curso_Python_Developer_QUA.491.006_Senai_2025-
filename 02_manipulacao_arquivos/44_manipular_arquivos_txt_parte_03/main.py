import os
# entrada  de dados
while True:
    try:
        novo_texto = input("Digite o texto :\n") # nao tem .strip pq o usuario vai digitar o texto todo da forma que quiser 
        nome_arquivo = input("Digite o nome do arquivo (sem extensão): ").strip().lower()  # .strip() remove espaços no inicio e no final da string, .lower() deixa tudo em minusculo
        with open(f"44_manipular_arquivos_txt_parte_03{nome_arquivo}.txt", "w", encoding="utf-8") as f:  # w de write modo escrita  # encoding o tipo de escrita do pt br  fazer um eyras   chamdo de f
            f.write(novo_texto)
            
        os.system("cls" if os.name == "nt" else "clear")  # limpa a tela do terminal, se for windows usa cls, se for linux ou mac usa clear
        print(f"Arquivo {nome_arquivo}.txt criado com sucesso!")  # mensagem de sucesso

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