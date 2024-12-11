def saudacao (hora_do_dia ):
    #dar bom dia 
    if (hora_do_dia >= 0) and (hora_do_dia <= 12):
        print ("bom dia  !!!")
    elif (hora_do_dia>=13) and (hora_do_dia<= 18):
          print ("boa tarde !!!")
    elif (hora_do_dia>=19) and (hora_do_dia<= 23):
          print ("boa noite !!!") 
    else:
        print("esse horario nao existe ")
 #fora daq funçao 
#peço  para o usuario o usuario dizer a hora do dia 
responda = int (input("digite que horas sao "))

saudacao(responda) 