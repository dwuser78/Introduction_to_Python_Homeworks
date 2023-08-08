def no_dup_sort(set):
    if len(set) < 2:
        return set
    else:
        pivot = set[0]
        less = [i for i in set[1:] if i < pivot]
        greater = [i for i in set[1:] if i > pivot]

        return no_dup_sort(less) + [pivot] + no_dup_sort(greater)

def check_entry_num(set, num):
    low = 0
    high = len(set) - 1

    while low <= high:
        mid = low + high
        guess = set[mid]
        if guess == num:
            return True
        if guess > num:
            high = mid - 1
        else:
            low = mid + 1

    return False

def get_numbers():
    set = []
    num = int(input('Enter the number of numbers: '))
    for i in range(num):
        set.append(int(input(f'Enter the value of the number [{i + 1}]: ')))

    return set

set_1 = no_dup_sort(get_numbers())
set_2 = no_dup_sort(get_numbers())

print("Numbers contained in both sets: ", end = "")
for value in set_1:
    if check_entry_num(set_2, value):
        print(value, end = " ")