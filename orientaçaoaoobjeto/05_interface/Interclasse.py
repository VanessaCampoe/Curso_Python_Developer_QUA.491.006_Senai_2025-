from abc import ABC
from abc import abstractmethod

# classe Abstrata
class Conta(ABC):
    @abstractmethod
    def __init__(self, saldo):
        # atributo private       
        self.__saldo = saldo

    # METODOS GET e SET
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
        

    # metodos de ação  -  que devo obrigar o programa a usar esses metodos
    @abstractmethod
    def consultar_dados(self):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

class ContaCorrente(Conta):
    def __init__(self, titular, cpf, agencia, num_conta, saldo):
        self.__titular = titular
        self.__cpf = cpf
        self.agencia = agencia
        self.__num_conta = num_conta
        super().__init__(saldo)


    # METODOS GET
    @property
    def titular(self):
        return self.__titular
    @property
    def cpf(self):
        return self.__cpf
    @property
    def agencia(self):
        return self.__agencia
    @property
    def num_conta(self):
        return self.__num_conta
    

    # METODOS SET
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia
    @num_conta.setter
    def num_conta(self, num_conta):
        self.__num_conta = num_conta

    # METODOS DA INTERFACE -  os que defini acima , para serem obrigatórios de usar ( CONSULTAR, DEPOSITAR e SACAR )
    def consultar_dados(self):
        print("  ----- 🐍🐍🐍 DADOS DA CONTA 🐍🐍🐍 -----  \n")
        print(f"Titular da Conta: {self.titular}")
        print(f"CPF: {self.cpf}")
        print(f"Numero da Agencia: {self.agencia}")
        print(f"Numero da Conta: {self.num_conta}")
        print(f"Saldo em Conta: R$  {self.saldo:.2f}")

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    
    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo
    
    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo
        # integridade e disponibilidades 









# # uma classe q nao e instanciada  ela e programada para mnao ser instacinada mais ela dtem herença , mas a sub nao ne abstrada e nao vai para hreanla pq ela nao fic aabistrada  
# # 
# from abc import ABC  # trabalha com metodos de abstração 

# from abc import abstractmethod
# #  uma classe abstrata  e uma classe que nao pode ser instanciada diretamente
# class Conta(ABC): # aqi ela herdeu da classe ABC , a herança e feita com parenteses e a super class  herdada da abc
#     @abstractmethod
#     def __init__(self,  saldo):
#         # atributo private 
#         # isso aqui seria o encapsulamento se eu fosse usar tudo encapsulamento
#         # self.__titular = titular
#         # self.__cpf = cpf
#         # self.__agencia = agencia
#         # self.__n_conta = n_conta
#         self.__saldo = saldo
        
        
#         # agora vamos defeini o metoso dele set e get
#         # aqui estamos setando o saldo
#         # self.__saldo = 0.0  # inicializando o saldo como zero v  
#         @property
#         def saldo(self):
#             return self.__saldo

#         @saldo.setter
#         def saldo(self, saldo):
#             self.__saldo = saldo
            
#             #  objetivo aqui e impedir a classe de ficar instanciada 
            
#     # classe conta que ter os metodos  aqu estou programando a interface 
#     @abstractmethod
#     def consultar_dados(self):
#         pass

#     @abstractmethod
#     def depositar(self, valor):
#         pass

#     @abstractmethod
#     def sacar(self, valor):
#         pass

# class ContaCorrente(Conta): # implemententa a classe conta 
#     def __init__(self, titular, cpf, agencia, conta,saldo):
#         self.__titular = titular
#         self.__cpf = cpf
#         self.__agencia = agencia
#         self.__n_conta = conta
#         super().__init__(saldo)
      
#       # metodos get e setter aqui aqui estou programando a interface
#     @property
#     def titular (self):
#         return self.__titular
    
#     @titular.setter
#     def titular(self, titular):
#         self.__titular = titular

#     @property
#     def cpf(self):
#         return self.__cpf

#     @cpf.setter
#     def cpf(self, cpf):
#         self.__cpf = cpf

#     @property
#     def agencia(self):
#         return self.__agencia

#     @agencia.setter
#     def agencia(self, agencia):
#         self.__agencia = agencia

#     @property
#     def n_conta(self):
#         return self.__n_conta

#     @n_conta.setter
#     def n_conta(self, n_conta):
#         self.__n_conta = n_conta
#  # os metoos terminam aqui o get  e setter 
 
 
#  # agora sim o metodo intereface 
#     def consultar_dados(self):
#         print(F"{'--'*20} dados da conta {'--'*20}  ")
#         print(f"Titular: {self.titular}")
#         print(f"CPF: {self.cpf}")
#         print(f"Agência: {self.agencia}")
#         print(f"Número da Conta: {self.n_conta}")
#         print(f"Saldo: {self.saldo:.2f}")

#     def depositar(self, valor):
#         self.saldo += valor
#         return self.saldo
  
    
#     def sacar(self, valor):
#         self.saldo -= valor
#         return self.saldo
   


# # @ abstrade e so para garantir a superclase para interface 
#     # def depositar(self, valor):
#     #     self.saldo += valor

#     # def sacar(self, valor):
#     #     if valor > self.saldo + self.__limite:
#     #         raise ValueError("Saldo insuficiente")
#     #     self.saldo -= valor