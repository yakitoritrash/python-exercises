def longestpal(s):
    res, resLen = "", 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            l, r, = i, j
            while l < r and s[l] == s[r]:
                l += 1
                r -= 1

            if l >= r and resLen < (j - i + 1):
                res = s[i : j + 1]
                resLen = j - i + 1
    print(res)
    return res

longestpal(input())
