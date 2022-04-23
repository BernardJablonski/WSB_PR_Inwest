from przeliczanie import *

def dasz_rade():
    plec = (input("Podaj plec(K/M): ")).lower()
    wiek = int(input("Podaj wiek: "))
    zdolnosc = int(input("3cia zmienna ktora nie wiem co robi wpisz 1 lub 2:"))
    x = (((plec == "k") + (wiek >= 18) + (zdolnosc == 1)))
    if x == 3:
        return True
