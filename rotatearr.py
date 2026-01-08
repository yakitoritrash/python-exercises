def rotate(arr, k):
    k = k % len(arr)
    l = 0
    r = len(arr) - 1
    while (l < r):
        arr[l], arr[r] = arr[r], arr[l]
        l+=1;
        r-=1;

    l = 0
    r = k - 1
    while (l < r):
        arr[l], arr[r] = arr[r], arr[l]
        l+=1;
        r-=1;

    l = k
    r = len(arr) - 1
    while (l < r):
        arr[l], arr[r] = arr[r], arr[l]
        l+=1;
        r-=1;
    return arr;

def main():
    arr = list(map(int, input().split()))
    print(arr)
    k = int(input())
    rotate(arr, k)
    print(arr)
main()


