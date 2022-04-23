plec = input("Podaj plec [K] (kobieta) lub [M] (mezyczyzna): ")

if plec == 'K':
        poziom_inv = input("Podaj kwote w USD: ")
        if poziom_inv.isdigit() == False:
            exit("Kwota musi być liczbą")
        poziom_inv = int(poziom_inv)
        if poziom_inv >= 100 :
            print("Inwestuj!")
        else:
            exit('jesteś za biedna na inwestycje, lepiej zacznij pracowac')

elif plec == "M":
        poziom_inv = input("Podaj kwote w USD: ")
        if poziom_inv.isdigit() == False:
            exit("Kwota musi być liczbą")
        poziom_inv = int(poziom_inv)
        if poziom_inv >= 10000:
            print("Inwestuj!")
        else:
            exit('jesteś za biedny na inwestycje, lepiej zacznij pracowac')