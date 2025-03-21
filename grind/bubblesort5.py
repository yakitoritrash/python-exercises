def bubblesort(arr):
    
    n = len(arr) - 1
    for i in range(n):
        for j in range(n - i):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp


    return arr

arr = [5, 3, 5, 8, 2, 10, 1]
print(bubblesort(arr))
