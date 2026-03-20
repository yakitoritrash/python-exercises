def cruise(t, e, l):
    current_guests=  0;
    max = 0;
    for i in range(t):
        current_guests += (e[i] - l[i]);
        if current_guests > max:
            max = current_guests;
    print(max);
    return max;






def main():
    t = int(input());
    e = list(map(int, input().split()));
    l = list(map(int, input().split()));
    cruise(t, e, l);



main();
