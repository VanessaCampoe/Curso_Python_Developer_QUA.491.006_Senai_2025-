#  composição e outro tiode relaçao um class e deve exitir para exiritiur outra relação e de fato um e objeto 
#  variaveis primiitiva e nativas 

#  criar uma nova class para cirar  e como a string do java q criaram uma class para ela pq ela nao e nativa 
#  diuas classes pessoas e veiculos 
#  atributos de seriam emial cpf 

import classes as c 

def main():  # aqui pode usar para interface grafica 
    
    proprietario = c.Pessoa(
        nome="",
        cpf="",
        email="",
        telefone="",
        endereco=""
    )

    carro = c.Veiculo(
        modelo="",
        fabricante="",
        cor="",
        placa="",
        ano="",
        proprietario="" 
    )


    print("Dados do proprietario:")
    # print(f"Nome: {proprietario.nome}")
    # print(f"CPF: {proprietario.cpf}")
    # print(f"Email: {proprietario.email}")
    # print(f"Telefone: {proprietario.telefone}")

 # entendeu a diferença e pelo amor de Deus nao esquece caralho 
# inputs
    proprietario.nome = input("Digite o nome do proprietario: ").strip().title()
    proprietario.cpf = input("Digite o CPF do proprietario: ").strip()
    proprietario.email = input("Digite o email do proprietario: ").strip().lower()
    proprietario.telefone = input("Digite o telefone do proprietario: ").strip()
    proprietario.endereco = input("Digite o endereco do proprietario: ").strip().title()


# dados do veiculo
#  no imput  ardem nao importa  por tando o professor começou pelo fabricante 

    carro.modelo = input("Digite o modelo do carro: ").strip().title()
    carro.fabricante = input("Digite o fabricante do carro: ").strip().title()
    carro.cor = input("Digite a cor do carro: ").strip().title()
    carro.placa = input("Digite a placa do carro: ").strip().upper()
    carro.ano = input("Digite o ano do carro: ").strip()
    

    carro.proprietario = proprietario
    # nao pode ser colacado antes 
    #  aqui atributo recebe meu objeto 
    # 1h
    print("\nDados do veiculo:")
    print(f"Modelo: {carro.modelo}")
    print(f"Fabricante: {carro.fabricante}")
    print(f"Cor: {carro.cor}")
    print(f"Placa: {carro.placa}")
    print(f"Ano: {carro.ano}")
    print(f"Dados do proprietario do veiculo \n: {carro.info_proprietario()}")


if __name__ == "__main__":
    main()