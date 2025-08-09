#conta corrente super class 
import Pessoasuperclasse as p 
import Contasuperclasse as c
# sub classe 

class ContaCorrente(p.Pessoasuperclasse, c.Contasuperclasse):  # as duas super classes nao podem ter relacao entre si e tem e=q ser claas e nao interface 
    
    def __init__ (self, nome, cpf, email, profissao, telefone, endereco, salario, agencia, numero , saldo):
        # atributos da super classe 
        p.Pessoasuperclasse.__init__(self, nome, cpf, email, profissao, telefone, endereco,salario) # definir todo os atributos de pessoas 
        c.Contasuperclasse.__init__(self, agencia, numero , saldo) # definir o atributos conta 
        # por ser um herança eu nao preciso fazer o get set , mas seu eu for colocar mais um atributo ai sim mas coloco no construtor 
        
    def exibir_dados(self):
        print("dados da conta : \n")
        p.Pessoa.exibir(self)  # chama o metodo exibir da super classe Pessoa
        c.Conta.exibir_dados(self)  # chama o metodo exibir_dados da super classe Conta
           
       
        # super().exibir_dados() nao exitete  me hernça 
        
 