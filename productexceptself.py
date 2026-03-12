def productExceptSelf(nums):
    res = {};
    for num in nums:
        product = 1;
        for i in nums:
            if i == num:
                continue;
            product *= i;
        res[num] = product;
    print(res.values());
    return res.values();

productExceptSelf([-1,1,0,-3,3]);
