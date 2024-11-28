# Função para calcular a média
def calcular_media(notas):
    # A função recebe uma lista de notas e retorna a média, somando as notas e dividindo pelo número de notas.
    return sum(notas) / len(notas)

# Função para determinar a situação do aluno com base na média e no número de faltas
def situacao_aluno(media, faltas):
    # Se o aluno tiver mais de 20 faltas, ele será reprovado por falta
    if faltas > 20:
        return "Reprovado por falta"
    # Se a média for 7 ou mais, o aluno é aprovado
    elif media >= 7:
        return "Aprovado"
    # Se a média for entre 5 e 6.99, o aluno está em recuperação
    elif media >= 5:
        return "Recuperação"
    # Se a média for menor que 5, o aluno é reprovado
    else:
        return "Reprovado"

# Função para obter os dados dos alunos e gerar o relatório final
def gerar_relatorio(num_alunos):
    alunos = []  # Inicializando a lista que armazenará os dados dos alunos
    
    # Loop que coleta os dados de cada aluno
    for i in range(num_alunos):
        # Exibe o número do aluno
        print(f"\nAluno {i+1}:")
        
        # Coleta o nome do aluno
        nome = input("Digite o nome do aluno: ")
        
        # Coleta o número de faltas do aluno
        faltas = int(input("Digite o número de faltas: "))
        
        # Lista para armazenar as notas do aluno
        notas = []
        
        # Loop para coletar as notas de 4 bimestres
        for j in range(4):  # Considerando 4 bimestres
            # Coleta a nota de cada bimestre e converte para float
            nota = float(input(f"Digite a nota do {j+1}º bimestre: "))
            # Adiciona a nota à lista de notas
            notas.append(nota)
        
        # Calcula a média das notas usando a função definida anteriormente
        media = calcular_media(notas)
        
        # Determina a situação do aluno com base na média e faltas
        situacao = situacao_aluno(media, faltas)
        
        # Cria um dicionário com as informações do aluno
        aluno = {
            "nome": nome,
            "faltas": faltas,
            "notas": notas,
            "media": media,
            "situacao": situacao,
        }
        
        # Adiciona o dicionário de dados do aluno à lista de alunos
        alunos.append(aluno)

    # Exibe o relatório final de todos os alunos
    print("\nRelatório final:")
    # Cabeçalho com a estrutura da tabela
    print(f"{'Nome':<20} {'Faltas':<7} {'Média':<6} {'Situação'}")
    print("-" * 50)

    # Loop para exibir as informações de cada aluno
    for aluno in alunos:
        # Imprime as informações do aluno no formato adequado
        print(f"{aluno['nome']:<20} {aluno['faltas']:<7} {aluno['media']:6.2f} {aluno['situacao']}")

# Função principal que inicia o programa
def main():
    # Pergunta ao usuário quantos alunos serão processados
    num_alunos = int(input("Digite o número de alunos: "))
    
    # Chama a função que gera o relatório com base no número de alunos
    gerar_relatorio(num_alunos)

# Executa o programa chamando a função main() quando o script é executado diretamente
if __name__ == "__main__":
    main()