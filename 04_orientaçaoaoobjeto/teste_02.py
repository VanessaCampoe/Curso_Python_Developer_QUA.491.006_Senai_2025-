#class pessoa:
# classe conta
class conta :
    # construtor 
    def __init__ (self,titular,cpf,agencia,numero_conta,saldo=0):
        self.titular = titular
        self.cpf = cpf 
        self.agencia = agencia 
        self.numero_de_conta = numero_conta 
        self.saldo = saldo
        
        #metodo de ação
    def consultar_dados(self):
        return (f"Titular: {self.titular}, CPF: {self.cpf}, Agência: {self.agencia}, "
                f"Número da Conta: {self.numero_de_conta}, Saldo: R$ {self.saldo:.2f}")
