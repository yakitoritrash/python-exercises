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


array = [2, 5, 7, 8, 10, 12]
number = 12

print(binsearch(array, number))


