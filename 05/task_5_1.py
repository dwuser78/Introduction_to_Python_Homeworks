def f(a: int, b: int):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * f(a, b - 1))   

print(f(3, 5))