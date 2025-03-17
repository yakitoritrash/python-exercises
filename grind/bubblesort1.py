def bubblesort(arr):
    
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tmp

    return arr


array = [5, 8, 1, 4, 9, 11, 6, 5, 20, 35, 1000]

print(bubblesort(array))
