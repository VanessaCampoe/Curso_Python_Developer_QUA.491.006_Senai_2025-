import modulo as mo 
if __name__ == "__main__":
    while True:
        print('1 - calcular primeiro grau   ')
        print('2 - calcular segundo grau    ')
        print('3 - limpar tela')
        opcao = input('Escolha uma opcao: ').strip()
        mo.limpar_tela()
        
        match opcao:
            
            
            case '1':
               
                
                try:
                    a = float(input('Digite o valor de a: ').replace(',', '.'))
                    b = float(input('Digite o valor de b: ').replace(',', '.'))
                    mo.limpar_tela()
                    
                    x = mo.primeiro_grau(a, b)
                    print(f"o valor de x é: {x}")
                    
                except Exception as e:
                    print(f'Erro: {e}')

                finally:
                    continue
              
              
              
            case '2':
                try:
                    a = float(input('Digite o valor de a: '))
                    b = float(input('Digite o valor de b: '))
                    c = float(input('Digite o valor de c: '))
                    mo.limpar_tela()
                    x = mo.segundo_grau(a, b, c)
                    for result in x:
                        print(f'{result}.')
                    #print(f"{x}.")
                except Exception as e:
                        print(f'Erro: {e}')

                finally:
                    continue
            case '3':
                
              
    
                
        
                print (" Comando encerrado .")
                break 
            case _:
                
                
                print('Opcao invalida. Tente novamente.')
                continue
            
    