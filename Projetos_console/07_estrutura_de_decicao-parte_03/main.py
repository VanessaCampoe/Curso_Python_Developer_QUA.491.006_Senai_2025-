aluno = input("Informe o nomedo aluno:")
media = float(input("Infome a médeia do aluno:").replace(",","."))

#estruturade decisao 
if media >= 0 and  media <= 10:
    if media>=7:
        print(f"{aluno}esta aprovado")
    elif media>=5 :
        print(f" {aluno}esta de recuperação .")
    else:
        pritn(f"{aluno} esta reprovado.")
    #TODO - 
    ...
else:
    print("Nota invalida .") 
