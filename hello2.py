import time 
n=int(input("Podaj liczę całkowitą"))
start=time.time()
for i in range(n):
    for j in range(n):
        print("#", end=" ")
        print()
        end=time.time()
        print(end-start)
        


        def silnia_rek(liczba):
            if liczba<2:
                return 1 
            else:
                return liczba*silnia_rek(liczba-1)
            print(silnia_rek(5))