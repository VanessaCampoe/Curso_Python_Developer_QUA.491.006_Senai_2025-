"""_summary_
# TODO - atividade: crie um porgrama de aplicativos de banco , onde:
- O usurrio crie uma conta bancária com os seguintes dados :
-- Titular da conta 
Cpf do titular
Agencia
Numero da conta
Saldo 

O usuario  pode fazer no programa 
consultar dados 
Depositar  valor 
Sacar valor 
Imprimir extrato(entenda-se: gerar arquivo com as dados da conta )
sair do programa 
#  NOTE - o nome do usurario e Conta
"""

class Conta:
    def __init__(self, titular, cpf, agencia, numero_conta, saldo=0):
        self.titular = titular
        self.cpf = cpf
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

    def consultar_dados(self):
        return (f"Titular: {self.titular}, CPF: {self.cpf}, Agência: {self.agencia}, "
                f"Número da Conta: {self.numero_conta}, Saldo: R$ {self.saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R$ {valor:.2f} realizado com sucesso!"
        else:
            return "Valor de depósito inválido."

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R$ {valor:.2f} realizado com sucesso!"
        else:
            return "Saldo insuficiente ou valor inválido."

    def imprimir_extrato(self):
        with open(f"{self.numero_conta}_extrato.txt", "w") as arquivo:
            arquivo.write(self.consultar_dados())
        return "Extrato gerado com sucesso!"