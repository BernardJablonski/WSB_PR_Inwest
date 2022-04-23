def przelicz():
    pln = float(input("Podaj ile PLN chcesz zainwestowac: "))
    kurs = float(input("Podaj kurs(zostaw puste aby wybrac autoamtyczny): "))
    print("Chcesz zainwestowac", pln * kurs, "USD")

przelicz()
