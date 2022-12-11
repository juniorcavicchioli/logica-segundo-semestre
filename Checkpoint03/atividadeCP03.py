# ADILSON ROBERTO CAVICCHIOLI JUNIOR...RM: 9XXXX TURMA: 1XXXX
# MATHEUS GOMES DA SILVA...............RM: 9XXXX
# VINICIUS PRADO MENDES................RM: 9XXXX
import random


# Funções do gerador de captcha
def captcha_(n, *args):
    """
    Cria uma sequência pseudo-aleatória de caracteres
    :param n: quantidade de caracteres
    :param args: caracteres que serão incluídos na sequência
    :return: string a sequência de caracteres
    """
    cha = ''
    for i in args:
        cha += i
    captcha = ''
    for i in range(n):
        captcha += random.choice(cha)
    return captcha


def quantidade_char():
    """
    Pede que digite e valida se foi digitado um número inteiro
    :return: int
    """
    while True:
        try:
            qnt = int(input("Digite a quantidade de caracteres: "))
            if qnt < 5:
                print("O número mínimo de caracteres é 5.")
            else:
                break
        except ValueError:
            print("Digite um número inteiro.")
    return qnt


def tipo_char():
    """
    Vê o tipo de caractere
    :return: uma string com os tipos de caracteres selecionados
    """
    while True:
        tipo = input("Tipos de caracteres:\n"
                     "(l)etras minúsculas\n"
                     "(L)etras maiúsculas\n"
                     "(d)ígitos\n"
                     "(e)speciais\n"
                     "-> ")
        char = ''
        controle = 0
        if 'l' in tipo:
            char += minusculas
            controle += 1
        if 'L' in tipo:
            char += maiusculas
            controle += 1
        if 'd' in tipo.lower():
            char += numeros
            controle += 1
        if 'e' in tipo.lower():
            char += especiais
            controle += 1
        if controle == 0:
            print("Insira ao menos um tipo de caractere. Ex. \"L d\"")
        else:
            break
    return char


def captcha_lista(num_char, type, alcance):
    """
    :param num_char: número de caracteres que terá cada captcha
    :param type: o tipo de caracteres que o captcha terá
    :param alcance: quantos elementos a lista terá
    :return: uma lista com cada captcha
    """
    captcha = []
    for i in range(alcance):
        captcha.append(captcha_(num_char, type))
    return captcha


# Funções da prova eletrônica
def alternativa(num):
    """
    Recebe um número da quantidade de alternativas e retorna uma letra equivalente
    :param num: número da quantidade de alternativas
    :return: letra equivalente
    """
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    return alfabeto[num]


def formatar(texto):
    """
    Recebe a lista de chaves de um dicionário como um string e retorna ele formatado para o programa.
    :param texto: string da lista de chaves de um dicionário.
    :return: string formatada.
    """
    texto = texto.replace('dict_keys([', '')
    texto = texto.replace("'", '')
    texto = texto.replace("])", '')
    texto = texto.split()
    texto[-2] = texto[-2].replace(',', ' &')
    texto = ' '.join(texto)
    return texto + '.'


# Programa principal
# Dicionários da prova eletrônica
dict_prova = {}
dict_questao = {}
dict_alternativas = {}
dict_pessoa = {}
# Listas com os caracteres do gerador de captcha
minusculas = 'abcdefghijklmnopqrstuvwxyz'
maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
especiais = '!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'

while True:
    menu_principal = input("==============-MENU PRINCIPAL-==============\n"
                           "1. Prova eletrônica\n"
                           "2. Gerador de captcha\n"
                           "0. Sair\n"
                           "-> ")
    if menu_principal == '1':
        while True:
            menu = input("\n==============-PROVA ELETRÔNICA-==============\n"
                         "1 - Admin\n"
                         "2 - Fazer a prova\n"
                         "0 - Sair\n"
                         "->")
            if menu == '1':
                menuADM = input("\n==============-ÁREA ADMINISTRTATIVA-==============\n"
                                "1 - Cadastrar questões\n"
                                "2 - Listar nomes | notas\n"
                                "0 - Voltar\n"
                                "->")
                if menuADM == '1':
                    while True:
                        try:
                            numQuestoes = int(input("Quantas questões você deseja cadastrar? "))
                            break
                        except (ValueError):
                            print("Insira um número válido. Ex: 4")
                    while True:
                        try:
                            numAlternativas = int(input("Quantas alternativas terão cada questão? "))
                            break
                        except (ValueError):
                            print("Insira um número válido. Ex: 4")
                    for i in range(numQuestoes):
                        enunciado = input(f"Questão {i + 1}: ")
                        dict_questao['enunciado'] = enunciado
                        for j in range(numAlternativas):
                            key = alternativa(j)
                            alter = input(key + ') ')
                            dict_alternativas[key] = alter
                        while True:
                            respCorreta = input(
                                f"Qual alternativa é a correta? {formatar(str(dict_alternativas.keys()))}"
                                f"\n-> ")
                            if respCorreta.lower() not in dict_alternativas.keys():
                                print("Insira uma alternativa das cadastradas.")
                                continue
                            else:
                                break
                        dict_questao['respCorreta'] = respCorreta
                        dict_questao['alternativas'] = dict_alternativas.copy()
                        key = 'questao ' + str(i + 1)
                        dict_prova[key] = dict_questao.copy()
                elif menuADM == '2':
                    if len(dict_pessoa) != 0:
                        for key, value in dict_pessoa.items():
                            print(f"O {key} tirou {value}")
                    else:
                        print("Ninguém concluiu a prova ainda.")
                elif menuADM == '0':
                    break
                else:
                    print("Insira uma opção válida.")
            elif menu == '2':
                if len(dict_prova) != 0:
                    nome = input("Digite o seu nome: ")
                    pontuacao = 0
                    for key in dict_prova.keys():
                        print(f"----------={key}=----------")
                        print(dict_prova[key]['enunciado'])
                        for keyX, valueX in dict_prova[key]['alternativas'].items():
                            print(f"{keyX}) {valueX}")
                        while True:
                            resposta = input("Sua resposta: ")
                            if resposta.lower() not in dict_prova[key]['alternativas'].keys():
                                print("Insira uma das alternativas")
                                continue
                            else:
                                break
                        if resposta.lower() == dict_prova[key]['respCorreta']:
                            pontuacao += 1
                        print("----------===+===----------\n")
                    qntPerguntas = len(dict_prova)
                    porcentagem = pontuacao / qntPerguntas * 100
                    dict_pessoa[nome] = porcentagem
                else:
                    print("Ainda não existem questões cadastradas")
            elif menu == '0':
                break
            else:
                print("Insira uma opção válida.")
    elif menu_principal == '2':
        while True:
            menu = input("========-Gerador de captchas-========\n"
                         "1. Captcha com 10 caracteres\n"
                         "2. Captcha definindo a quantidade de caracteres\n"
                         "3. Captcha definindo a quantidade e o(s) tipo(s) de caractere(s)\n"
                         "4. Gravando/Exibindo numa lista\n"
                         "5. Gravando/Exibindo num arquivo\n"
                         "0. Sair\n"
                         "-> ")
            print("========-=-=-========")
            if menu == '1':
                print("Captcha:", captcha_(10, minusculas, maiusculas, numeros, especiais))
            elif menu == '2':
                qnt = quantidade_char()
                print("Captcha:", captcha_(qnt, minusculas, maiusculas, numeros, especiais))
            elif menu == '3':
                qnt = quantidade_char()
                char = tipo_char()
                print("Captcha:", captcha_(qnt, char))
            elif menu == '4':
                qnt = quantidade_char()
                char = tipo_char()
                captcha = captcha_lista(qnt, char, 10)
                print("=-------------------=")
                for i in range(len(captcha)):
                    print(f"Captcha {i+1}: {captcha[i]}")
                print("=-------------------=")
            elif menu == '5':
                qnt = quantidade_char()
                char = tipo_char()
                captcha = captcha_lista(qnt, char, 10)
                file = open("captchas.txt", "w+")
                for i in range(len(captcha)):
                    if captcha[i] == captcha[-1]:
                        file.write(f"{captcha[i]}")
                    else:
                        file.write(f"{captcha[i]}\n")
                file.seek(0)
                file_text = file.read().split("\n")
                print("=-------------------=")
                for i in range(len(file_text)):
                    print(f"Captcha {i+1}: {file_text[i]}")
                print("=-------------------=")
            elif menu == '0':
                break
            else:
                print("Digite uma opção válida.")
    elif menu_principal == '0':
        print("O macado está acenando! Tchau :)")
        break
    else:
        print("Digite uma opção válida.")