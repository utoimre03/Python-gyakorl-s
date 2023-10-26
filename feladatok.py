import math

def elso():
    szam = 0
    while szam < 150:
        if szam % 2 == 0:
            print(szam, end="; ")
        szam += 1
    print(150, end="")

def masodik():
    osztharom = 0
    sorszam = 1

    while sorszam <= 10:
        szam = int(input("Kérem, adja meg a(z) "+str(sorszam)+". számot:"))
        if szam % 3 == 0:
            osztharom += 1
        sorszam += 1
    print("A bekért számok alapján "+str(sorszam)+" olyan szám van, amely 3-mal osztható.")

def harmadik():
    szam = 1
    while szam % 10 != 0:
        szam = int(input("Kérem, adjon meg egy egész számot!"))
    print(szam)

def negyedik():
    szam = int(input("Kérem adjon meg egy olyan számot, ami kétjegyű és páros: "))
    while not((((szam >= 10) and (szam <= 99)) or ((szam >= -99) and (szam <= -10))) and (szam % 2 == 0)):
        szam = int(input("Kérem adjon meg egy olyan számot, ami kétjegyű és páros: "))

def otodik():
    szam = int(input("Kérem, adjon meg egy egész számot: "))
    while not(szam <= 0) and (szam % 2 == 0):
        szam = int(input("Kérem, adjon meg egy egész számot: "))

def hatodik():
    szam = int(input("Kérem, adjon meg egy egész számot: "))
    while not(szam % 3 == 0 or (math.sqrt(szam) == int(math.sqrt(szam)))):
        szam = int(input("Kérem, adjon meg egy egész számot: "))
    print(szam)

def hetedik():
    a = int(input("Kérem adjon meg egy egész számot: "))
    b = int(input("Kérem adjon meg egy egész számot: "))
    c = int(input("Kérem adjon meg egy egész számot: "))
    print("A 3szög megszerkeszhető.")
    while not (a + b >= c and b + c >= a and a + c > b):
        print("Nem szerkeszthető 3szög.")
        a = int(input("Kérem adjon meg egy egész számot: "))
        b = int(input("Kérem adjon meg egy egész számot: "))
        c = int(input("Kérem adjon meg egy egész számot: "))

def nyolcadik():
   szoveg = str(input("Kérem, írjon be egy szöveget: "))
   while len(szoveg) < 3:
       szoveg = str(input("Kérem, írjon be egy szöveget: "))
   print(szoveg.upper())

def kilencedik():
    szoveg = str(input("Kérem, írjon be egy szöveget: "))
    while not (szoveg == szoveg.lower() and len(szoveg) > 4):
        print("Próbálkozzon kisbetűkkel! (Minimum 4 betű)")
        szoveg = str(input("Kérem, írjon be egy szöveget: "))

def tizedik():
    szam = int(input("Kérem, adjon meg számokat. Jelezze 0-val, amennyiben nem kíván több számot beírni!"))
    while not (szam == 0):
        szam = int(input("Kérem, adjon meg számokat. Jelezze 0-val, amennyiben nem kíván több számot beírni!"))

