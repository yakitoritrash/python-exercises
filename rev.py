def main():
    x = str(input())
    for c in range(len(x) - 1, 0, -1):
        print(x[c], end="")

main()
