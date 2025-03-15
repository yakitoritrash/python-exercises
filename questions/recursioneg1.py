def foo(n):
    if n == 1:  #base case
        return 1
    
    out = n + foo(n-1)  #recurse
    print(n)    #post  
    return out


print(foo(100))
