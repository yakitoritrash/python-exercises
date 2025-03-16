def binsearch(arr, n):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:  
        m = int((lo + (hi-lo)//2))
        v = arr[m]

        if v == n: 
            #print(arr[v])
            return m
        elif v > n:
            hi = m - 1
        else:
            lo = m + 1
    
    return -1

array = [2, 4, 5, 6, 7, 8, 11]
number = 2
print(binsearch(array, number))

