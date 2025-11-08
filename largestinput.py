def largestinput(n):
    arr = []
    n = str(n)
    for i in range(len(n)):
        arr.append(int(n[i]))
    arr = sorted(arr, reverse=True)
    for i in range(len(n)):
        arr[i] = str(arr[i])
    arr = "".join(arr)
    return arr

x = int(input())
print(largestinput(x))
