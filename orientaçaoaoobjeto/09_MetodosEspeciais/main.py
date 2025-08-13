import Pessoa

def main():
    usuario = Pessoa.Pessoa(nome="Nessa", idade=40)
    
    print(usuario)
    print(f" Idade:{len(usuario)} anos")
    
# destruiçao do obejto 
    del (usuario)

    #  print(usuario) se ele for colocado depois vai dar erro pq o usuario foi deletado

if __name__ == "__main__":
    main()