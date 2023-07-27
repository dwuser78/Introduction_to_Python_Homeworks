import random
import math

def pick_numbers():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    return num1, num2

def calc_numbers(s, p):
    d = s * s + 4 * p
    x = s / 2 + math.sqrt(d) / 2
    y = s / 2 - math.sqrt(d) / 2
    return x, y

x, y = pick_numbers()
s = x + y
p = x * y

print(f"The sum of the hidden numbers: {s}")
print(f"Multiplication of hidden numbers: {p}")

x, y = calc_numbers(s, -p)
print("Hidden numbers:")
print(f"x = {int(x)}; y = {int(y)}")