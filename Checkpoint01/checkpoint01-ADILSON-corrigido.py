# ADILSON ROBERTO CAVICCHIOLI JUNIOR RM:9XXXX
# delta = negativo a=1, b=2.45/2 c=20
# delta = 0 a=1 b=2 c=1 ou a=10 b=0 c=0
# delta positivo a=1 b=-5 c=6

from math import sqrt


def calculoDelta(a, b, c):
    return b*b - 4 * a * c


def raizDeltaZero(a, b):
    return -b / (2 * a)


def primeiraRaiz(a, b, delta):
    return (-b + sqrt(delta)) / (2 * a)


def segundaRaiz(a, b, delta):
    return (-b - sqrt(delta)) / (2 * a)


cont = "1"
while cont == "1":
    print("Uma equação de segundo grau é ax² + bx + c = 0")
    a = float(input("Insira o valor de a: "))
    b = float(input("Insira o valor de b: "))
    c = float(input("Insira o valor de c: "))
    print(f"\nEquação montada: {a}x² + {b}x + {c} = 0")
    delta = calculoDelta(a, b, c)
    if a == 0:
        print("Esta equação é de primeiro grau e não de segundo.")
    elif b == 0 or c == 0:
        print("Essa é uma equação de segundo grau, porém é incompleta já b e(ou) c é(são) 0.")
    else:
        print("Essa é uma equação de segundo grau completa.")

    print(f"O valor de delta é {delta}")

    if delta < 0:
        print("Valor de delta negativo. Não há raíz de um número negativo.")
    elif delta == 0:
        print(f"Como o valor de delta é 0, existe apenas uma raiz: {raizDeltaZero(a,b)}")
    else:
        print(f"Valor de delta positivo. A primeira raiz é {primeiraRaiz(a, b, delta)} e a segunda é "
              f"{segundaRaiz(a, b, delta)}")

    while True:
        cont = input("Deseja fazer outro cálculo? \n[1]Sim\n[2]Não\n-> ")
        if cont == "2" or cont == "1":
            break
        elif cont != "1" and cont != "2":
            print("Escolha uma opção válida.")

print("O macaco está ascenando. Tchau!")
