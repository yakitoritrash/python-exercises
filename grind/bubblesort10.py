def bubblesort(arr):

    n = len(arr) - 1
    for i in range(n):
        for j in range(n - i):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp

    return arr

arr = [3, 4, 5, 6, 2, 30, 1, 11, 6]

print(bubblesort(arr))
