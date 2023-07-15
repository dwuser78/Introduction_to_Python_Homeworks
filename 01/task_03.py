n = 123321

tmp_n = n
digits = 0
sum_left = 0
sum_right = 0

while tmp_n > 0:
    tmp_n //= 10
    digits += 1

half_num = digits // 2

while n > 0:
    if digits > half_num:
        sum_right += n % 10
    else:
        sum_left += n % 10
    n //= 10
    digits -= 1

if sum_left == sum_right:
    print('yes')
else:
    print('no')