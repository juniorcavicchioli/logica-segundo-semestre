# ADILSON ROBERTO CAVICCHIOLI JUNIOR RM:9XXXX
# delta = negativo a=1, b=2.45/2 c=20
# delta = 0 a=1 b=2 c=1 ou a=10 b=0 c=0
# delta positivo a=1 b=-5 c=6

import math

def delta(a, b, c):
    return b*b - 4 * a * c

def raizDeltaZero(a, b):
    return -b/(2*a)

def primeiraRaiz(a, b, delta):
    return (-b + math.sqrt(delta)) / (2 * a)

def segundaRaiz(a, b, delta):
    return (-b - math.sqrt(delta)) / (2 * a)

def continuar():
    i = True
    while i:
        cont = str(input("Deseja continuar? {S}Sim ou {N}Não.\n"))
        if cont == "s" or cont == "S":
            i = False
            return True
        elif cont == "n" or cont == "N":
            i = False
            return False
        else:
            print("Escolha entre {S}Sim ou {N}Não.")

print("Uma equação de segundo grau é ax² + bx + c = 0")
a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))
print(f"\nEquação montada: {a}x² + {b}x + {c} = 0")

delta = delta(a, b, c)

cont = True
while cont:
    if a == 0:
        print("Esta equação não é de segundo grau mas sim de primeiro.")
        cont = False
    else:
        if b == 0 or c == 0:
            print("Equação de segundo grau Incompleta, b ou c é(são) 0.")
            cont = continuar()
            if not cont:
                break
            print(f"O valor de delta é {delta}")
            cont = False
        elif b != 0 or c != 0:
            print("Equação de segundo gau Completa\n")
            cont = continuar()
            if not cont:
                break
            print(f"Delta é igual a {delta}")
        if delta < 0:
            cont = continuar()
            if not cont:
                break
            print("Valor de delta negativo. Não há raiz de número negativo")
            cont = False
        elif delta == 0:
            cont = continuar()
            if not cont:
                break
            print(f"Como o valor de delta é 0, existe apenas uma raiz: {raizDeltaZero(a, b)}")
            cont = False
        else:
            cont = continuar()
            if not cont:
                break
            print(f"Valor de delta é positivo. A primeira raiz é {primeiraRaiz(a, b, delta)} e a segunda é {segundaRaiz(a, b, delta)}")
            cont = False
