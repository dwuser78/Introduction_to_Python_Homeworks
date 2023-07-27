import random
import time

def verify_approval(pred, num_pred):
    for i in range(1, num_pred):
        if i == 1:
            left_exp = pred[i - 1]
            print(f"not({pred[i - 1]}", end=" or ")

        left_exp = left_exp or pred[i]

        if i < num_pred - 1:
            print(f"{pred[i]}", end=" or ")
        else:
            left_exp = not left_exp
            print(f"{pred[i]}) = {left_exp}")

    for i in range(1, num_pred):
        if i == 1:
            right_exp = not pred[i - 1]
            print(f"not {pred[i - 1]}", end=" and ")

        right_exp = right_exp and not pred[i]

        if i < num_pred - 1:
            print(f"not {pred[i]}", end=" and ")
        else:
            print(f"not {pred[i]} = {right_exp}")

    return left_exp == right_exp

pred = []
num_pred = random.randint(3, 15)
attempts = 100
fails = []
result = True

start_time = time.time()

for i in range(num_pred):
    pred.append(random.choice([True, False]))

for i in range(attempts):
    print(f"Verification of approval. Attempt: {i}")
    if verify_approval(pred, num_pred):
        print("The statement is true.")
        print("--------------------------------------")
    else:
        print("The statement is false.")
        print("--------------------------------------")
        fails.append(i)
        result = False

end_time = time.time()

print(f"The statement is true in {attempts - len(fails)} attempts out " +
      f"of {attempts}.")

if not result:
    print("Failed attempts:", end = " ")
    for fail in fails:
        print(fail, end = " ")

print(f"Time spent: {round(end_time - start_time, 3)} s.")