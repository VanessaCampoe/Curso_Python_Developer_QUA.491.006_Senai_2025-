class Pessoa:  # super classe  e toda classe q vai forner metodos para classes  pai 
    # 
    def __init__(self, nome, cpf, email, profissao, telefone, endereco,salario):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.profissao = profissao
        self.telefone = telefone
        self.endereco = endereco
        self.salario = salario
        
        
        @property
        def nome(self):
            return self.__nome 


        @nome.setter
        def nome(self, nome):
            self.__nome = nome
            
        @property
        def cpf(self):
            return self.__cpf
        

        @cpf.setter
        def cpf(self, cpf):
            self.__cpf = cpf

        @property
        def email(self):
            return self.__email

        @email.setter
        def email(self, email):
            self.__email = email

        @property
        def profissao(self):
            return self.__profissao

        @profissao.setter
        def profissao(self, profissao):
            self.__profissao = profissao

        @property
        def telefone(self):
            return self.__telefone

        @telefone.setter
        def telefone(self, telefone):
            self.__telefone = telefone

        @property
        def endereco(self):
            return self.__endereco

        @endereco.setter
        def endereco(self, endereco):
            self.__endereco = endereco

        @property
        def salario(self):
            return self.__salario

        @salario.setter
        def salario(self, salario):
            self.__salario = salario
            
            
            
            
def exibir (self):
        print("=== Dados da Conta Corrente ===")
        print("Nome:", self.get_nome())
        print("CPF:", self.get_cpf())
        print("Email:", self.get_email())
        print("Profissão:", self.get_profissao())
        print("Telefone:", self.get_telefone())
        print("Endereço:", self.get_endereco())
        print("Salário:", self.get_salario())
        print("Agência:", self.get_agencia())
        print("Número da Conta:", self.get_numero())
        print("Saldo:", self.get_saldo())