import Hclasse as c 
import os 
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # instancia de classes 
    usuario = c.PessoaFisica(nome="", cpf="", telefone="", endereco="")
    empresa = c.PessoaJuridica(nome_fantasia="", cnpj="", telefone="", endereco="") # aqui e como se fosse o scanner do java 
    # se for init devo colocar o zero e sem aspas  0 para int e 0.0 para float
    # agora vou setar os atrributos 
     # input do usuario 
     # imput do usuario 
   
    
    
    print ("Encontre como os dados do usuario:\n")
    usuario.nome = input("Digite o nome: ").strip().title()
    usuario.cpf = input("Digite o CPF: ").strip()
    usuario.telefone = input("Digite o telefone : ").strip()
    usuario.endereco = input("Digite o endereço: ").strip().title()


    limpar()

    # input da empresa 
    
    print ("Encontre como os dados do empresa:\n")

    empresa.nome_fantasia = input("Digite o nome fantasia: ").strip().title()
    empresa.cnpj = input("Digite o CNPJ: ").strip()
    empresa.telefone = input("Digite o telefone : ").strip()
    empresa.endereco = input("Digite o endereço: ").strip().title()


    
    #output dos dados
    limpar()
    print("Dados do usuário:")
    usuario.exibir_dados()
    
    print("Dados da empresa:")
    empresa.exibir_dados()
    

if __name__ == "__main__":
    main()
    # nao temos atributos modificadores no python
    #aqui poe ser o def 
    # as funçoes devem ser declaradas as da dunção princia
     # polimorfismo vc tem 2 classes diferentes fazendo ou nao herança com metodos com o mesmo nome so que elas agem de forma diferente 
 