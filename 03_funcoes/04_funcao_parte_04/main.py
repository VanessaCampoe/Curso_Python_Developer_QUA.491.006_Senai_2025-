# funcao 
From modulo import limpar_tela, velocidade_media, tempo_medio, acelerarcao_medio

# algoritmo principal 
if __name__ == "__main__":
    v = 0
    while True:
        print("1 - calcular velocidade média")
        print("2 - calcular tempo médio")
        print("3 - Sair do programa")
        opcao = input("Escolha uma opção: ")
        limpar_tela()
        
        
        match opcao:
            case "1":
                try:
                    vi = float(input("informe a velocidade inicial: ")).replace(",", ".")
                    vf = float(input("informe a velocidade final: ")).replace(",", ".")
                    v = velocidade_media(vi, vf)

                    print(f"velocidade média: {v} m/s")
                    
                except Exception as e:
                    print(f"Erro: {e}")
                finally:
                    continue 
                
            case "2":
                try:
                    t = float(input("Informe o tempo: ")).replace(",", ".")
                    limpar_tela()
                    if v is not 0:
                        
                        a = acelerarcao_medio(v, t)
                        
                        print(f"Aceleração média: {a} m/s²")
                    else:
                        print("Sem informação de velocidade média.")
                except Exception as e:
                    print(f"Erro: {e}")
                finally:
                    continue

                   

            case "3":
                print("programa encerrado.")
                break
            
            case _:
                  print("Opção inválida. Tente novamente.")
                  continue              
         