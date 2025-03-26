import random

def generuj_haslo(dlugosc):

    znaki = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    haslo = ""

    for i in range(dlugosc):

        haslo += random.choice(znaki)

    return haslo


dlugosc = int(input("Podaj długość hasła: "))

haslo = generuj_haslo(dlugosc)

print("Twoje hasło to:", haslo) 