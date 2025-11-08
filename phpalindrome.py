def ispalindrome(s):
    s = s.lower().replace(" ", "");
    t = ""
    for c in s:
        if c.isalpha():
            t += c
    l = 0
    r = len(t) - 1
    while l < r:
        if t[l] != t[r]:
            return False
        l+=1;
        r-=1;
    return True;


print(ispalindrome("a man, a plan, a Canal - Panama!"))


