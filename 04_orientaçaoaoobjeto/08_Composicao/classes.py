# sempre começar por classes 
#  aqui e uma concerssiorai a de veiuclos 
class Pessoa:
    def __init__(self, nome, cpf, email, telefone, endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone
        self.__endereco = endereco

        @property
        def nome(self):
            return self.__nome

        @property
        def cpf(self):
            return self.__cpf

        @property
        def email(self):
            return self.__email

        @property
        def telefone(self):
            return self.__telefone

        @property
        def endereco(self):
            return self.__endereco
        
        @nome.setter
        def nome(self, nome):
            self.__nome = nome

        @cpf.setter
        def cpf(self, cpf):
            self.__cpf = cpf

        @email.setter
        def email(self, email):
            self.__email = email

        @telefone.setter
        def telefone(self, telefone):
            self.__telefone = telefone

        @endereco.setter
        def endereco(self, endereco):
            self.__endereco = endereco

# metodo que retorna os dados da pessoa 
def obter_dados(self):
    return f'Nome: {self.nome}, CPF: {self.cpf}, Email: {self.email}, Telefone: {self.telefone}, Endereco: {self.endereco}\n'

#classe veiculo 
class Veiculo:
    def __init__(self, modelo, fabricante, cor ,placa, ano, proprietario):
        self.__modelo = modelo
        self.__placa = placa
        self.__ano = ano
        self.__cor = cor
        self.__fabricante = fabricante
        self.__proprietario = proprietario   # objeto da classe Pessoa fazendo papel de atributo .
        # nao fiz lista pq vai ser so um proprietario
        
        
        
        # definindo os getters e setters

        @property
        def modelo(self):
            return self.__modelo

        @property
        def placa(self):
            return self.__placa

        @property
        def ano(self):
            return self.__ano

        @property
        def cor(self):
            return self.__cor
        @property
        def fabricante(self):
            return self.__fabricante

        @property
        def proprietario(self):
            return self.__proprietario

        @modelo.setter
        def modelo(self, modelo):
            self.__modelo = modelo

        @placa.setter
        def placa(self, placa):
            self.__placa = placa

        @ano.setter
        def ano(self, ano):
            self.__ano = ano

        @cor.setter
        def cor(self, cor):
            self.__cor = cor
            
        @fabricante.setter
        def fabricante(self, fabricante):
            self.__fabricante = fabricante

        @proprietario.setter
        def proprietario(self, proprietario):
            self.__proprietario = proprietario

        def info_proprietario(self):
            return self.__proprietario.obter_dados()
        