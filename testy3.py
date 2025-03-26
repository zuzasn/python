def sito_eratostenesa(n):
   
    sita = [True] * (n + 1)
    sita[0] = sita[1] = False  
    
    for i in range(2, int(n**0.5) + 1):  
        if sita[i]:
            for j in range(i*i, n+1, i):  
                sita[j] = False
    
    
    liczby_pierwsze = [i for i in range(2, n + 1) if sita[i]]
    return liczby_pierwsze


n = 70
print(f"Liczby pierwsze do {n}: {sito_eratostenesa(n)}")
