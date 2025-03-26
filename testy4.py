def szyfr_cezara(tekst, przesuniecie):
    wynik = ""
    for znak in tekst:
        if znak.isalpha():
            kod = ord(znak) + przesuniecie
            if znak.islower():
                if kod > ord('z'):
                    kod -= 26
            elif znak.isupper():
                if kod > ord('Z'):
                    kod -= 26
            wynik += chr(kod)
        else:
            wynik += znak
    return wynik

tekst = input("Podaj tekst do zaszyfrowania: ")
przesuniecie = int(input("Podaj wartość przesunięcia: "))

print("Zaszyfrowany tekst:", szyfr_cezara(tekst, przesuniecie))
