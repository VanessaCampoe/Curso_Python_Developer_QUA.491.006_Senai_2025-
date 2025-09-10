# criar objetos
# primeiro passo para criar um objeto da classe ContaCorrente
import ContaCorrentesubclasse as cc
# função main
def main():
    
    # intancia do objeto 
    # aqui ele e meu objeto essa conta por  ser com letra minuscula

    conta = cc.ContaCorrentesubclasse(
        nome="" 
        cpf=", 
        email="", 
        profissao="",
        telefone="", 
        endereco="", 
        salario=0, 
        agencia="", 
        numero="", 
        saldo=0
    )
    # exibir dados da conta
    conta.exibir_dados()
    

#inpede a importaçaõ 
if __name__ == "__main__":
    main()
    
