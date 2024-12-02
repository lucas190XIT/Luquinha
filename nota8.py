
#ENTRADA
#solicitar a entrada do aluno
pontos = int(input ("pontos: "))

#PROCESSAMENTO
#verificar qual a nota do aluno com base
if pontos >= 90 and pontos <= 100:
    print(("A")) #SAIDA - exibir a nota para o usuario 
elif pontos >= 80 and pontos < 90:
    print ("B")
elif pontos >= 70 and pontos < 80:
    print ("C")
elif pontos >= 60 and pontos < 70:
    print ("D")
else:
    print("F")


#SAÍDA
#EXIGIRA A NOTA PARA O USUARIO