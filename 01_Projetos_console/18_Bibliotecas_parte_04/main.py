# importando apenas uma parte da biblioteca 
from datetime import date 
dia = date.today().strftime("%d/%m/%Y")
# exibe a data de hj 
#se o y for maiusculo a data fica com 4 digitos 
# se o y for minusculo ele fica com doi digitos no ano 
print(dia) 