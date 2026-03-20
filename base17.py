def main():
    x = input().strip();
    y = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16,
         "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15, "g": 16}
    result = 0;
    length = len(x);
    for i, c in enumerate(x):
        power = length - i - 1;
        if c.isdigit():
            result += (17 ** power) * int(c);
        else:
            result += y[c] * (17 ** power);
    print(result);


main();
