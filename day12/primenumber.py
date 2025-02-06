def is_prime(num):
    if num ==  2:
        print("True") 
    else:

        for i in range(2, (num//2) + 1):
            if num%i == 0:
                x = False
                break
            else:
                x = True
        print(x)

is_prime(75)
