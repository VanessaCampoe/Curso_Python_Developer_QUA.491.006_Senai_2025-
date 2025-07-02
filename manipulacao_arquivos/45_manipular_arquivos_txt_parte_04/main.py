try:
    

    arquivo = input ("informe  o nome do arquivo (sem extensão) :").strip().lower()
    with open(f"{arquivo }.txt", "r", encoding="utf-8") as f:
        texto = f.read()
        print(texto)
        novo_texto = input("Digite o novo texto para substituir o arquivo: ")
        with open(f"{arquivo}.txt", "w", encoding="utf-8") as f_write:
            f_write.write(novo_texto)
        
except Exception as e:
    print(f"Não foi possível ler o arquivo. {e}")