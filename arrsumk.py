def arrsumk(arr1, arr2, k):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2, reverse=True)

    for i in range(len(arr1)):
        if (arr1[i] + arr2[i] < k):
            return False

        return True


print(arrsumk([2, 1, 3], [7, 8, 8], 10))


