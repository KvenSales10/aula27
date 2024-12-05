escolha_menu = int(input("escolja uma opcao \n1.cadrastar\n2.relatorio\n3.encerrar\nescolha uma dessas opiçoes "))

if escolha_menu == 1:

    aluno = []
    cont  = 0
    escolher_usuario = int(input("quantos alunos voce deseja cadastrar:"))
    while cont <escolher_usuario:
        nome= input("digite o nome do aluno:")
        nota1 =float(input("digite a nota do 1ºbimestre:"))
        nota2 =float(input("dgite a nota do 2ºbimestre:"))
        nota3 =float(input("digite a nota do 3ºbimestre:"))
        nota4 = float(input("digite a nota do 4ºbimestre:"))
        faltas = int(input("digite a quantidade de faltas do aluno: "))

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
        cont=+1



    #relatorio
print(aluno)
print("\n----------------------------------------------")
print("relatorio do da media do aluno  ")
print (f"nome:{nome}")
print (f"notas:{nota1,nota2,nota3,nota4}")
print(f"faltas:{faltas}")
print (f"media:{media}")
print(f"a sitquaçao do aluno e: {situaçao}")
print("-------------------------------------------------")        
