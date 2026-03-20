def cycle(arr, k):
    l = 0;
    r = len(arr) - 1;
    while (l < r):
        arr[l], arr[r] = arr[r], arr[l];
        l+=1;
        r-=1;
    l = 0;
    r = k - 1;
    while (l < r):
        arr[l], arr[r] = arr[r], arr[l];
        l+=1;
        r-=1;

    l = k;
    r = len(arr) - 1;
    while (l < r):
        arr[l], arr[r] = arr[r], arr[l];
        l+=1;
        r-=1;
    print(arr);
    return arr;


def main():
    arr = list(map(int, input().split()));
    k = int(input());
    cycle(arr, k)
main();

