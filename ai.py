from random import randrange, choice

def tah(pole, pozice, symbol):
    """vrátí herní pole s daným symbolem umístěným na danou pozici"""
    return pole[:pozice] + symbol + pole[pozice + 1:]

def velikost_pole():
    #hráč si zvolí, na jak velkém poli bude hrát
    delka = int(input("Na jak velkém poli chceš hrát? (4 a víc) "))
    while delka <= 4:
        delka = int(input("Větší než čtyři, prosím: "))
    return delka

delka_pole = velikost_pole() #uložíme do proměnné, ať se s tím dá počítat

def tah_pocitace(pole):
    #dva seznamy, aby si to mohlo vybrat, jestli nahradí před nebo po znaku
    nahrada1 = ["-HP", "PH-"]
    nahrada2 = ["-PP", "PP-"]
    while True:
        #nejdřív, že když to jde, má se snažit vyhrát
        if "PP-" in pole:
            return pole.replace("PP-", "PPP")
        elif "-PP" in pole:
            return pole.replace("-PP", "PPP")
        elif "P-P" in pole:
            return pole.replace("P-P", "PPP")
        #pak že to má odvrátit nebezpečí
        elif "H-H" in pole:
            return pole.replace("H-H", "HPH", 1)
        elif "-H-" in pole:
            return pole.replace("-H-", choice(nahrada1), 1)
        elif "HH-" in pole:
            return pole.replace("HH-", "HHP", 1)
        elif "-HH" in pole:
            return pole.replace("-HH", "PHH", 1)
        #pak že se to má snažit přidávat ke svým
        elif "-P-" in pole:
            return pole.replace("-P-", choice(nahrada2), 1)
        elif "--P" in pole:
            return pole.replace("--P", "-PP", 1)
        elif "P--" in pole:
            return pole.replace("P--", "PP-", 1)
        else:
            pozice = randrange(0, delka_pole)
            if pole[pozice] == '-':
                return tah(pole, pozice, 'P')

    if (pole == "") or ("-" not in pole):
        raise Exception("je to nějaké polámané, zkus to znovu")
