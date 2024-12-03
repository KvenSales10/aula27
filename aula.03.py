cont  = 0
escolher_usuario = int(input())
while cont <escolher_usuario:
    nome= input()
    nota1 =float(input())
    nota2 =float(input())
    nota3 =float(input())
    nota4 = float(input())

    faltas = int(input())

    media = (nota1+nota2+nota3+nota4)/4


    if faltas >31:
        situaçao = "reprovado por falta "
    elif media >=8:
        situaçao ="aprovado"
    elif media >=5:
        recuperaçao = float(input())
        if recuperaçao >=(10-media):
          situaçao = "aprovado na recupertaçao"
          print(situaçao)
    else:
        situaçao="aprovado na recuperaçao "
        print(situaçao)
else:
    situaçao ="aprovado por media "

    #relatorio
    print("\n----------------------------------------------")
    print("tudo sobre o o aluno aqui ")
    print (f"nome{nome}")
    print (f"notas:{nota1,nota2,nota3,nota4}")
    print(f"faltas:{faltas}")
    print (f"media:{media}")
    print(f"a airuaçao do aluno e {situaçao}")
    print("-------------------------------------------------")        
    cont+=1