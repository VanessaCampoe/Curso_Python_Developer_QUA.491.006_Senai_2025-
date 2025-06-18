import datetime 
#hora = datetime.datetime.now()
 #hora = datetime.datetime.now()# aqui mostra a data e hora atual
# aqui mostra data e hora , mas quero so a hora entao vamos usar o comando strftime
#hora = datetime.datetime.now().strftime("%H:%M:%S")
#print(hora)
from datetime import datetime

hoje = datetime.today().strftime("%d/%m/%Y")
# exibe a data de hoje
hora = datetime.datetime.now().strftime("%H:%M:%S")
print(f"Data de execução:{hoje}.")
print(f"Hora de execução:{hora}.")