def bubble_sort(arr):
    n = len(arr)
    
  
    for i in range(n):
   
        for j in range(0, n-i-1):
       
            if arr[j] > arr[j+1]:
             
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr


lista = [90, 34, 25, 189, 22, 11, 9]
posortowana_lista = bubble_sort(lista)
print("Posortowana lista:", posortowana_lista)
