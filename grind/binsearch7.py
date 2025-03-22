def binsearch(arr, n):
    hi = len(arr) - 1
    lo = 0

    while lo <= hi:
        m = lo + (hi-lo)//2
        v = arr[m]
        if v == n:
            return m
        elif v > n:
            hi = m - 1
        else:
            lo = m + 1

    

arr = [2, 3, 4, 5, 6]
n = 5

print(binsearch(arr, n))
