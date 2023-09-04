def sum(a: int, b: int):
    if (b == 0):
        return (a)
    return sum(a+1,b-1)

print(sum(2, 3))