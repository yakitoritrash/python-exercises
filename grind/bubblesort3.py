
def bubblesort(arr):

    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tmp

    return arr


arr = [6, 4, 2, 9, 1, 0]

print(bubblesort(arr))
