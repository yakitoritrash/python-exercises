def encode(strs):
    str = "";
    for s in strs:
        str += f"{len(s)}&{s}";
    print(str);
    return str

encode(["hello", "world"]);
def decode(str):
    strs, i = [], 0;
    while i < len(str):
        j = i;
        while str[j] != "&":
            j += 1;
        length = int(str[i:j])
        strs.append(str[j + 1: j + 1 + length]);
        i = j + 1+ length;
    
    print(strs);
    return strs;
str = "5&hello5&world"
decode(str);
