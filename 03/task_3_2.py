list_1 = [1, 12, 6, 7, 8, 15]
k = 11

min = abs(k - list_1[0])
near_val_idx = 0

for i in range(1, len(list_1)):
    next = abs(k - list_1[i])

    if next < min:
        min = next
        near_val_idx = i

print(list_1[near_val_idx])