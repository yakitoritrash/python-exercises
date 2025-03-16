def binsearch(arr, n):

    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        m = (lo + (hi-lo)//2)
        v = arr[m]

        if v == n:
            return m
        elif v > n:
            hi = m - 1
        else:
            lo = m + 1

array = [1, 2 , 5, 6, 7, 8, 11]
number = 8

print(binsearch(array, number))
