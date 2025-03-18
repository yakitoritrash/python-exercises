def binsearch(arr, n):
    hi = len(arr) - 1
    lo = 0

    while lo <= hi:
        m = (lo + (hi-lo)//2)

        v = arr[m]

        if v == n:
            return m
        elif v > n:
            hi = m - 1
        else:
            lo = m + 1


array = [2, 4, 6, 8, 9, 100]

number = 6

print(binsearch(array, number))
