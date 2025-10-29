def mult(x, y):
    return x * y
def add(x, y):
    return x + y

def mathi(math_func):
    def func(x):
        return math_func(x, x);
    return func;

square_func = mathi(mult);
doub = mathi(add)

print(square_func(5));
print(doub(5));

