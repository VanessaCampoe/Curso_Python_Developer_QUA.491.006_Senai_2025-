from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base    # e oq e vai gerar uma tabela n banco 

try:
    engine = create_engine("sqlite:///01_crud_uma_entidade/database/db_crud.db")  # aqui e so uma instancia por isso nao criou o bd # aqui fica a unica klinha de codigo que eu preciso mudar para pode usar o msql ///!SECTION  começar a colocar o caminho de onde o databe vai ficar 
    #NOTE - engine para o MySQL e coloca r mais o driv 
    # engine = create_engine("MySQL+mysqlconnector:///senha:root@localhost:3306/nome_banco") 
    Base = declarative_base( ) # se tiver representando pode ter a letra maiuscula e ele esta funcionando como herença 
    
    class pessoa(Base):
        __tablename__ = "pessoa"
        id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
        nome =  Column(String, nullable=False)
        email = Column(String, nullable=False,unique=True)
        data_nascimento = Column(Date, nullable=False)
    
    Base.metadata.create_all(engine)
        
        #  e como se fosse o 2.09
        # f1 abrir buscar  depois open data base  escolheer nosso crud 
        
        
except Exception as e :
    print(f"Não foi possivel conectar ao banco.{e} ")
    
    
    
    
    
    
    
    #prepared statement /// uma aplicação /// uma camada de proteção , faz uma consulta indireta 
    # sql injection // um tipo de ataque haker entra em uma pag de internt e na barra de navegação e insere um sql isso pq usavam o get  hj usam postpela maquina dele ele consegue acesso direto no servidor 
    