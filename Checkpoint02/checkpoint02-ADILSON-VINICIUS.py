#ADILSON ROBERTO CAVICCHIOLI JUNIOR - RM: 9XXXX
#VINICIUS PRADO MENDES - RM: 9XXXX

def formatacao(bra):
    """
    :param bra: texto que será formatado
    :return: o texto com os caracteres necessários para alinhar a tabela
    """
    tamanho = 29 - len(bra)
    msg = bra + ' ' * tamanho
    return msg

pessoa = {}
situacao = {}
disciplinas = []
menu = 'i'
while menu != '0':
    menu = input("CADASTRO ALUNOS | DISCIPLINAS\n"
                 "-----------------------------\n"
                 "0 - SAIR\n"
                 "1 - Cadastrar o aluno\n"
                 "2 - Cadastrar as disciplinas\n"
                 "3 - Listar o registro Completo\n"
                 "\nOpção desejada: ")
    if menu == '1':
        print("CADASTRANDO O ALUNO\n"
              "-----------------------------\n")
        while True:
            rm = input("RM........: ")
            if 0 < len(rm) <= 6:
                pessoa['rm'] = rm
                break
            else:
                print("Insira um RM válido! Ex: 123456")
        pessoa['nome'] = input("Nome......: ")
        pessoa['turma'] = input("Turma.....: ")
    elif menu == '2':
        menu2 = "corinthians"
        print("\nCADASTRAR AS DISCIPLINAS | NOTAS | STATUS \n"
              "------------------------------------------")
        while menu2 != ".":
            situacao['disciplina'] = menu2 = input("Disciplina........: ")
            if menu2 != ".":
                situacao['media'] = float(input("Média anual.......: "))
                if situacao['media'] >= 6:
                    situacao['status'] = "Aprovado"
                else:
                    situacao['status'] = "Reprovado"
                print(f"Status............: {situacao['status']}\n")
                disciplinas.append(situacao.copy())

    elif menu == '3':
        print("\nLISTANDO O REGITRO COMPLETO\n"
              "---------------------------")
        print(f"RM: {pessoa['rm']} | NOME: {pessoa['nome']} | TURMA: {pessoa['turma']}")
        print(f"\nDISCIPLINAS                     MF     STATUS\n"
              f"------------------------------------------------")
        for i in range(0, len(disciplinas)):
            print(f"{formatacao(disciplinas[i]['disciplina'])} | {disciplinas[i]['media']} | {disciplinas[i]['status']}")
        print("")
    else:
        print("Digite uma opção válida.")