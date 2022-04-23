
wiek = input("Podaj wiek: ")
# Sprawdzamy, czy wiek jest złożony z cyfr
if wiek.isdigit() == False:
    exit("Wiek musi być liczbą")
wiek = int(wiek)
if wiek >= 18 and wiek <= 60:
    print("Inwestuj")
elif wiek > 60:
    print("Jesteś już za stary na inwestycje")
else:
    exit('jesteś za stary!')