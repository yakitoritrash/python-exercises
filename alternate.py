def alt(s):
    odd = 0;
    even = 0;
    for i, c in enumerate(s):
        if (i % 2 != 0):
            odd += int(c)
        else:
            even += int(c)
    res = abs(odd - even);
    print(res);
    return res;
def main():
    s = input();
    alt(s);
main();
