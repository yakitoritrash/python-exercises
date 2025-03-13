from math import sqrt

def crystalballs(breaks):
    jmpAmount = int(sqrt(len(breaks)))
    i = jmpAmount
    while i < len(breaks):
        if breaks[i]:
            break
        i += jmpAmount

    i -= jmpAmount

    for j in range(jmpAmount):
        if i < len(breaks) and breaks[i]:
                return i
        i += 1

    return -1z

breaks = [False] * 12 + [True] * 11

print(crystalballs(breaks))

