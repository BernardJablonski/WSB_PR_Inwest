
pln = int(input("Podaj ile PLN chcesz zainwestowac: "))
kurs = int(input("Podaj kurs(zostaw puste aby wybrac autoamtyczny): "))
if kurs == 0:
    print(f"Chcesz zainwestowac {pln*4.7}USD")
else:
    print(f"Chcesz zainwestowac {pln * kurs}USD")

