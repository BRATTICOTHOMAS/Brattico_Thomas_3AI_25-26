#la bubble sort è piu lento della shell sort e della python sort
#quest'ultima è un'ottimizzazione della shell sort

def shell_sort(arr): #codice shell sort
    n = len(arr)
    gap = n // 2   # gap iniziale

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Inserimento con gap
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2   # riduzione gap

    return arr

# Esempio d'uso
lista = [12, 34, 54, 2, 3]
print(shell_sort(lista))

































