aluno = []
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
        else:
            situaçao="aprovado na recuperaçao "
    else:
        situaçao ="reprovado por media "
    aluno.append([nome,faltas,media,situaçao])
    cont+=1
    #relatorio
print(aluno)
print("\n----------------------------------------------")
print("tudo sobre o o aluno aqui ")
print (f"nome{nome}")
print (f"notas:{nota1,nota2,nota3,nota4}")
print(f"faltas:{faltas}")
print (f"media:{media}")
print(f"a airuaçao do aluno e {situaçao}")
print("-------------------------------------------------")        