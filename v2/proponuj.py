from przeliczanie import *

x = przelicz()


def aktywahej():
    if x <= 0:
        print("Nie poszalejesz mistrzu, na gume kulke nie starczy")
    elif x <= 50:
        print("Najpierw pomysl o jedzeniu dla dzieci")
    elif x <= 200:
        print("Inwestuj w orlen")
    elif x <= 2000:
        print("mieszkanie najlepsza inwestycja")
    else:
        print("Otwórz hodowle jedwabników")

