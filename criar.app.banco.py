#cadrasto de usuario e senha 
#menu principal 
while True:

    print("bem vindo! \n digit 1 cadrastra, 2 login, 3 encerrar ")

    #ler a escolha do usuario 
    escolha_menu = int(input()) #escolha um menu

    #se usuario escolher cartao 
    if escolha_menu  == 1:
        #crie uma usuario e uma senha com tipo string  
        usuario = input ("crie um nome de usuario ")
        senha = input ("crie uma senha ")
    elif escolha_menu == 2: #se o usuario escolher login 
        #conparar a inf. cadrastadas com uma leitura 
        login_usuario = input("digite seu usuario")
        login_senha = input("digite sua senha")
        if login_usuario == usuario and login_senha == senha:
            print ("loguin realizado com sucesso ")
            print("bem vindo ",usuario )
            while True:
                print ("1. depoisito ,2. sacar ,3. extrato 4. encerrar ")
                print ("")
                if escolha_principal ==1:
                    valor_depositado = float (input())
                    saldo = saldo + valor_deposito 
             
    else:
        print ("usuario ou senha incvorreto")
        ou senha incorreta ")