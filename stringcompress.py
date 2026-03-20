def stringcom(s):
    compressed = []
    count = 1;
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1;
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1;
    compressed.append(s[-1] + str(count));

    result = "".join(compressed);
    if (len(result) < len(s)):
        print(result);
        return result;
def main():
    s = input();
    stringcom(s);

main()
            
