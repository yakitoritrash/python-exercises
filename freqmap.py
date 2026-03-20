def first_unique_char():
    s = input();
    freqmap = {};
    for c in s:
        if c not in freqmap:
            freqmap[c] = 1;
        else:
            freqmap[c] += 1;
    for key, value in freqmap.items():
        if value == 1:
            print(key);
            return
    print(freqmap);

first_unique_char();

