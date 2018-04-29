#from random import randrange
import ai
from copy import deepcopy

# defaultni predpoklad
symbol_komplu = "o"
symbol_hrace = "x"

def nastav_symbol_hrace():
    #hráč si vybere, co chce být
    symbol = input("Chceš být kolečko nebo křížek? ")
    while (symbol != "x" and symbol != "o"):
        print("Křížek nebo kolečko, nic jiného.")
        symbol = input("Tak co si vybereš? ")
    if symbol == "o":
        # chci menit globalni promenne, proto je nutno je zde nadeklarovat jako global
        global symbol_komplu
        global symbol_hrace
        symbol_komplu = "x"
        symbol_hrace = symbol

# zde se vybere, kdo ma co
nastav_symbol_hrace()

def print_pole(pole):
    temp = deepcopy(pole)
    temp = temp.replace('H', symbol_hrace)
    temp = temp.replace('P', symbol_komplu)
    print(temp)

def vyhodnot(pole):
    """vyhodnotí, jestli hra skončila a někdo vyhrál, nebo jestli hrajeme dál"""
    if "HHH" in pole:
        return "H"
    elif "PPP" in pole:
        return "P"
    elif "-" not in pole:
        return "!"
    else:
        return "-"

def tah_hrace(pole):
    """hráč táhne na pozici, kterou si vybral"""

    while True:
        position = input("Na jaké pozici chceš táhnout? 1-20 ")

        try:
            pozice = int(position) - 1
        except ValueError:
            print("Mělo by to být číslo...")
        else:

            if (pozice < 0) or (pozice > 19):
                print("Má to být číslo od 1 do 20.")
            elif pole[pozice] != "-":
                print("Tam už někdo hrál.")
            else:
                return ai.tah(pole, pozice, 'H')

def piskvorky1d():
    """zahraje hráč, zahraje počítač, vyhodnotíme, furt dokola, dokud je kam hrát"""

    pole = "--------------------"
    print_pole(pole)

    while vyhodnot(pole) == "-":
        pole = tah_hrace(pole)
        print_pole(pole)

        if vyhodnot(pole) == "-":
            pole = ai.tah_pocitace(pole)
            print_pole(pole)
        else:
            break

    if vyhodnot(pole) == 'H':
        print ("Vyhrálas!")
    elif vyhodnot(pole) == 'P':
        print ("Vyhrál stroj.")
    elif vyhodnot(pole) == "!":
        print("Nevyhrála nikdo.")
