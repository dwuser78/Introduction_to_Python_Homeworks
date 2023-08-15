import random

_NUM_ELEM = 10
_MIN_ELEM = 1
_MAX_ELEM = 1000

def gen_list(num_elem: int, min_elem: int, max_elem: int) -> list:
    res_list = []

    for i in range(num_elem):
        res_list.append(random.randint(min_elem, max_elem))

    return res_list

def print_list(msg: str, src_list: list):
    if msg != "":
        print(f"{msg} ", end="")

    for elem in src_list:
        print(elem, end=" ")

    print()

def find_range(src_list: list, begin_dgt: int, end_dgt: int) -> list:
    res_list = []

    for i in range(len(src_list)):
        if src_list[i] >= begin_dgt and src_list[i] <= end_dgt:
            res_list.append(i)

    return res_list

src_list = gen_list(_NUM_ELEM, _MIN_ELEM, _MAX_ELEM)
print_list("Source list:", src_list)

begin = int(input("\nEnter the beginning of the range: "))
end = int(input("Enter the end of the range: "))

idx_list = find_range(src_list, begin, end)
print_list("\nElements from the range have indexes:", idx_list)