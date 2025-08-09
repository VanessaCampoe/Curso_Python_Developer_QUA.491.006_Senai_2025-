import modulo as mo 
if __name__ == "__main__":
    while True:
        try:
            n = int(input("Digite um número: ")) 
            print(f"Fatorial de {n} ! ={mo.fatorial(n)}")
            opcao = input("Escolha :").strip()
            match opcao:
                case "1":
                    n = int(input("Digite um número: ")) 
                    print(f"Fibonacci de {n} ! = {mo.fibonacci(n)}")
                    continue
                
                case "2":
                    
                    print(f"programa encerrado ")
                    break
               
                case _:
                    print("Opção inválida")
                          
            
        except Exception as e :
            print(f"Erro: {e}")
            break
    
    
    
    
    
    
    
    
    print(mo.soma(1, 2))
    print(mo.subtracao(5, 3))
    print(mo.multiplicacao(4, 2))
    print(mo.divisao(8, 2))