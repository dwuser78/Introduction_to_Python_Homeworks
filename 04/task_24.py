import random

_MIN_BERRIES = 1
_MAX_BERRIES = 50

def get_init_data():
    bushes = []
    num_bushes = int(input('Enter the number of berry bushes: '))

    for i in range(num_bushes):
        bushes.append(random.randint(_MIN_BERRIES, _MAX_BERRIES))

    return num_bushes, bushes

num_bushes, bushes = get_init_data()

for i in range(num_bushes):
    print(f"{bushes[i]} berries have grown on bush #{i + 1}")

if bushes[1] > bushes[num_bushes - 2]:
    max_per_step = bushes[0] + bushes[num_bushes - 1] + bushes[1]
else:
    max_per_step = bushes[0] + bushes[num_bushes - 1] + bushes[num_bushes - 2]

for i in range(1, num_bushes - 1):
    if (bushes[i - 1] + bushes[i] + bushes[i + 1]) > max_per_step:
        max_per_step = bushes[i - 1] + bushes[i] + bushes[i + 1]

print(f"The max number of berries harvested in one step: {max_per_step}")