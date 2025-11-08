import math
def sumofprimes(x):
    arr = []
    while (x % 2 == 0):
        arr.append(2)
        x = x//2
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        while x % i == 0:
            arr.append(i)
            x //= i
    if x > 2:
        arr.append(x)

    count = 0;
    for i in range(len(arr)):
        count += arr[i]

    return count 



print(sumofprimes(38))

