def bubblesort(arr):
    
    n = len(arr)

    for i in range (n):
        for j in range (n - 1 - i):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp

    return arr

arr = [6, 4, 7, 2, 9, 1]

print(bubblesort(arr))
