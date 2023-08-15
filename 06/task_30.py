def calc_progression(a1: int, n: int, d: int) -> list:
    an = []

    for i in range(n):
        an.append(a1 + i * d)

    return an

a1 = int(input("Enter the first term of the progression: "))
n = int(input("Enter the number of elements of the progression: "))
d = int(input("Enter the difference of progression: "))

print("Elements of progression: ", end="")
for elem in calc_progression(a1, n, d):
    print(elem, end=" ")