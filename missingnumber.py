def missingnumber():
    arr = list(map(int, input().split()));
    n = len(arr)
    expected_sum = (n * (n + 1)) // 2;
    actual_sum = sum(arr);
    print(expected_sum - actual_sum);



