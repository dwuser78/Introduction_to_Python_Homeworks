def print_operation_table(operation, num_rows=6, num_columns=6):
    for row in range(1, num_rows + 1):
        for col in range(1, num_columns + 1):
            print(operation(row, col), end=" ")
        print()

print_operation_table(lambda x, y: x * y)