from random import randrange, choice

def tah(pole, pozice, symbol):
    """vrátí herní pole s daným symbolem umístěným na danou pozici"""
    return pole[:pozice] + symbol + pole[pozice + 1:]

def tah_pocitace_obsolete(pole):
    """vrátí pole se zaznamenaným tahem počítače"""
    pozice = randrange(0, 20)
    while pole[pozice] != "-":
        pozice = randrange(0, 20)
    return tah(pole, pozice, 'P')

def tah_pocitace(pole):
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
        elif "-H-" in pole:
            return pole.replace("-H-", choice(nahrada1))
        elif "HH-" in pole:
            return pole.replace("HH-", "HHP", 1)
        elif "-HH" in pole:
            return pole.replace("-HH", "PHH", 1)
        elif "H-H" in pole:
            return pole.replace("H-H", "HPH", 1)
        #pak že se to má snažit přidávat ke svým
        elif "-P-" in pole:
            return pole.replace("-P-", choice(nahrada2))
        elif "--P" in pole:
            return pole.replace("--P", "-PP", 1)
        elif "P--" in pole:
            return pole.replace("P--", "PP-", 1)
        else:
            pozice = randrange(0, 20)
            if pole[pozice] == '-':
                return tah(pole, pozice, 'P')
