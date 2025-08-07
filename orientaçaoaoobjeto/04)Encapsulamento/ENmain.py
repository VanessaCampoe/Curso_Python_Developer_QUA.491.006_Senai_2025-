# comentar sempre onde for objeto ou classe ou função metodo
# tipos de encapsulamento  public, protected ,private
import ENclasse as c 
import os 
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
def main(): # funcao criando 
    # instancia de classes  ou criação do obejo todo  contrsutor e um q cria o obejto 
    # todo instancia de classe chama o construtor e faz meu obejto 
    #obejto ou instancia de classe
    # aqui eu estou importando a classe pessoa e criando o obejo usuario e empresa
    usuario = c.PessoaFisica(nome="", cpf="", telefone="", endereco="") # objeto 
    empresa = c.PessoaJuridica(nome_fantasia="", cnpj="", telefone="", endereco="") # obejto 
    # aqui e como se fosse o scanner do java 
    # se for init devo colocar o zero e sem aspas  0 para int e 0.0 para float
    # agora vou setar os atrributos 
     # input do usuario 
     # imput do usuario 
   
    
    # sentando os valores do usurio 
    print ("Encontre como os dados do usuario:\n") 
    
    
    
    # aqui eu seto os atributos
    # metodo set 
    usuario.nome = input("Digite o nome: ").strip().title() 
    usuario.cpf = input("Digite o CPF: ").strip()
    usuario.telefone = input("Digite o telefone : ").strip()
    usuario.endereco = input("Digite o endereço: ").strip().title() # aqui eu seto os atributos


    limpar()  # 

    # input da empresa 
    
    print ("Encontre como os dados do empresa:\n")

    empresa.nome_fantasia = input("Digite o nome fantasia: ").strip().title()
    empresa.cnpj = input("Digite o CNPJ: ").strip()
    empresa.telefone = input("Digite o telefone : ").strip()
    empresa.endereco = input("Digite o endereço: ").strip().title()

 #output dos dados
    limpar() 

    #chamdo do metodo get
    print("Dados do usuário:\n")
    print(f"Nome do usuario: {usuario.nome}")
    print(f"CPF do usuario: {usuario.cpf}")    
    print(f"Telefone usuario: {usuario.telefone}")
    print(f"Endereço usuario: {usuario.endereco}\n")
    
    print("Dados do usuário:\n")
    print(f"Nome do usuario: {empresa.nome_fantasia}")
    print(f"CPF do usuario: {empresa.cnpj}")
    print(f"Telefone usuario: {empresa.telefone}")
    print(f"Endereço usuario: {empresa.endereco}\n")


    # print("Dados do usuário:") # 
    # usuario.exibir_dados() 
    
    # print("Dados da empresa:")
    # empresa.exibir_dados()
    
    
if __name__ == "__main__": 
    main()
    # nao temos atributos modificadores no python
    #aqui poe ser o def 
    # as funçoes devem ser declaradas as da dunção princia
        # polimorfismo vc tem 2 classes diferentes fazendo ou nao herança com metodos com o mesmo nome so que elas agem de forma diferente
        # encapsulamento tem o objetivo de esconder atributos 
        # e metodos de uma classe para que nao sejam acessados diretamente de fora da classe
        # encapsulamento é uma forma de proteger os dados e garantir que eles sejam acessados0