# Função para calcular a média
def calcular_media(notas):
    return sum(notas) / len(notas)

# Função para determinar a situação do aluno
def situacao_aluno(media, faltas):
    if faltas > 20:
        return "Reprovado por falta"
    elif media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "reprovado"
    
    #funçao para obter os dados e gerar o relatoprio
    def gerar_relatorio(num_aluno):
        aluno = {}

        #coletando todos os dados dos alunos 
        for i in range(num_alunos):
            print(f"/nAluno {i+1}:")
            nome =input("digite o nome do aluno:")
            faltas = int(input("digite o numero de faltas: "))
            totas = []
            
            #coletando as notas 
            for j in range(4): #considerando o 4 bimestre 
                nota = float(input("digite nota do {j+1}º bimestre"))
                nota.appnd(nota)

                media = calcular_media(notas)
                situaçao = situaçao_aluno(media, faltas)

                aluno = {
                    "nome":nome,
                    "faltas":faltas,
                    "notas":notas,
                    "media":media,
                    "situaçao":situaçao,
                    }
                alunos.append(aluno)

                #exibindo o relatorio 
                print("/nRelatorio final:")
                print(f"{'nome':<20} {'faltas':<7} 'media' :<6 {'sitiaçao'}")
                print("-"*50)

                for aluno in alunos:
                    print (f"{aluno['nome']:<20} {aluno['faltas']:<7} {aluno['media']:6.2f} {aluno['situaçao']}")
                          
                    #funçao principal
                    def main():
                        num_alunos = int(input("digite o numero de alunos:" ))
                        gerar_relatorio(numalunos)
                        #executar  o programa 
                        if __name__ == "__main__":
                            main()