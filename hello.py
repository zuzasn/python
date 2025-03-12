def kalkulator():
   print("Prosty kalkulator")
   print("Dostępne operacje: +, -, *, /")
   try:
       liczba1 = float(input("Podaj pierwszą liczbę: "))
       operacja = input("Podaj operację (+, -, *, /): ")
       liczba2 = float(input("Podaj drugą liczbę: "))
       if operacja == '+':
           wynik = liczba1 + liczba2
       elif operacja == '-':
           wynik = liczba1 - liczba2
       elif operacja == '*':
           wynik = liczba1 * liczba2
       elif operacja == '/':
           if liczba2 != 0:
               wynik = liczba1 / liczba2
           else:
               print("Błąd: Dzielenie przez zero!")
               return
       else:
           print("Błąd: Nieznana operacja!")
           return
       print(f"Wynik: {wynik}")
   except ValueError:
       print("Błąd: Niepoprawna liczba!")
kalkulator()



