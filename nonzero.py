def nonzero(arr):
    arr2 = [];
    zerarr = [];
    for a in arr:
        if a != 0:
            arr2.append(a);
        else:
            zerarr.append(a);
    (arr2.extend(zerarr));
    print(arr2);


def main():
    n = int(input());
    arr = [];
    while n > 0:
        x = int(input());
        arr = list(map(int, input().split()));
        nonzero(arr);
        n-=1;


main();
