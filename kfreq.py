def kfreq(nums, k):
    count = {};
    res = [];
    numvalues = [];
    for num in nums:
        if num not in count:
            count[num] = 0;
        count[num] += 1;

    arr = []
    print(nums);
    print(count);
    for num, cnt, in count.items():
        print([cnt, num]);
        arr.append([cnt, num]);
    print(arr);
    arr.sort();
    print(arr);
    while len(res) < k:
        res.append(arr.pop()[1]);
    print(res);
    return res;
    for value in count.values():
        numvalues.append(value);
    for s in sorted(numvalues, reverse=True):
        for key, value in count.items():
            if (value == s):
                res.append(key);

    #print(sorted(numvalues));
    #print(count);
    print(res[:k]);

#nums = [4,1,-1,2,-1,2,3]
#k = 2;
nums = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
k = 10;
kfreq(nums, k);
