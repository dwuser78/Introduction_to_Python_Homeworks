def all_divisors(num):
    iter = 1
    divisors = []

    while iter ** 2 <= num:
        if num % iter == 0:
            divisors.append(iter)
            if iter != num // iter:
                divisors.append(num // iter)
        iter += 1

    divisors.sort()

    return divisors

num = int(input('Enter the number: '))

divisors = all_divisors(num)

print(f"All divisors for the number {num}: {divisors}")