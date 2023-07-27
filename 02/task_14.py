curr_num = 1
n = int(input('Enter the limit: '))

if n <= curr_num:
    print(f"{n} - is the wrong number, set a larger one.")
    exit(1)

print(f"All integer powers of two from 1 to {n}:")
if curr_num == 1:
        print(curr_num, end=" ")

while curr_num < n:
    if curr_num * 2 < n:
        curr_num *= 2
        print(curr_num, end=" ")
    else:
        break