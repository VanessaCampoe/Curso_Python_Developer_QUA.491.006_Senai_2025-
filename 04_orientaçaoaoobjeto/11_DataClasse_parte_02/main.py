import PessoaFisica
import PessoaJuridica
import os 


limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = PessoaFisica.PessoaFisica(email="", telefone="", endereco="", nome="", cpf="", idade=0)

    empresa = PessoaJuridica.PessoaJuridica(email="", telefone="", endereco="", razao_social="", nome_fantasia="", cnpj="")
    
    
    
        
    # input do usuario 
    print("Informe os dados da Pessoa Fisico ")
    usuario.email = input("E-mail: ")
    usuario.telefone = input("Telefone: ")
    usuario.endereco = input("Endereço: ")
    usuario.nome = input("Nome: ")
    usuario.cpf = input("CPF: ")
    usuario.idade = int(input("Idade: "))
    limpar()
    print("\nInforme os dados da Pessoa Juridica ")
    empresa.email = input("E-mail: ")
    empresa.telefone = input("Telefone: ")
    empresa.endereco = input("Endereço: ")
    empresa.razao_social = input("Razão Social: ")
    empresa.nome_fantasia = input("Nome Fantasia: ")
    empresa.cnpj = input("CNPJ: ")

    limpar()

    # output

    print(usuario)
    print(empresa)
    
if __name__ == "__main__":
    main()
    
    # print dos dados
    # print("Dados da Pessoa Física:")
    # print(f"E-mail: {usuario.email}")
    # print(f"Telefone: {usuario.telefone}")
    # print(f"Endereço: {usuario.endereco}")
    # print(f"Nome: {usuario.nome}")
    # print(f"CPF: {usuario.cpf}")
    # print(f"Idade: {usuario.idade} anos")

    # print("\nDados da Pessoa Jurídica:")
    # print(f"E-mail: {empresa.email}")
    # print(f"Telefone: {empresa.telefone}")
    # print(f"Endereço: {empresa.endereco}")
    # print(f"Razão Social: {empresa.razao_social}")
    # print(f"Nome Fantasia: {empresa.nome_fantasia}")
    # print(f"CNPJ: {empresa.cnpj}")