_HEX_FORMAT = 16
_OCT_FORMAT = 8

def dec_to(base: int, dec_num: int) -> str:
    res = ""
    sym_set = "0123456789ABCDEF"
 
    while dec_num > 0:
        res = sym_set[dec_num % base] + res
        dec_num //= base

    return res

dec_num = int(input('Enter the decimal number: '))

print("The number {} in HEX notation: {}".format(dec_num,
                                                 dec_to(_HEX_FORMAT, dec_num)))
print("The number {} in OCT notation: {}".format(dec_num,
                                                 dec_to(_OCT_FORMAT, dec_num)))