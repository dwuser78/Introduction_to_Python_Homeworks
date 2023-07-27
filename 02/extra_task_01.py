import decimal

num = decimal.Decimal(input('Enter the number: '))
sum = 0

while num - int(num) != 0:
    num *= 10

while num > 0:
    sum += num % 10
    num //= 10

print(f"The sum of the digits in the number = {int(sum)}")