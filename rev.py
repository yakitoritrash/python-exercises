import binascii
import base64
def main():
    x = str(input())
    x = binascii.unhexlify(x).decode()
    x = x[::-1]
    #for c in range(len(x) - 1, 0, -1):
    #    print(x[c], end="")
    x = base64.b64decode(x).decode()
    print(x)

main()
