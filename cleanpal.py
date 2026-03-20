def cleanpy():
    s = input().strip();
    l = 0;
    r = len(s) - 1;
    while l < r:
        if not s[l].isalnum():
            l += 1;
        elif not s[r].isalnum():
            r -= 1;
        else:
            if (s[l].lower() != s[r].lower()):
                print("False");
                return False
            l+=1;
            r-=1;
    print("True");

cleanpy();

