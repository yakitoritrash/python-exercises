def foo(n):
    if n == 1:
        return 1
    
    out = n + foo(n-1)
    print(n)
    return out


print(foo(100))
