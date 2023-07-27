import random

def flip_coins(n):
    coins = []
    for i in range(0, n):
        coins.append(random.randint(0, 1))
    return coins

# "h" - heads (1)
# "t" - tails (0)

def show_coins(coins):
    print("Coin:", end="|")
    for i in range(0, len(coins)):
        print(f" {i + 1} ", end="|")
    print("")

    print("Side:", end="|")
    for coin in coins:
        if coin == 0:
            side = 't'
        else:
            side = 'h'
        print(f" {side} ", end="|")
    print("")

heads = 0
tails = 0
coins_num = 5
coins = flip_coins(coins_num)

show_coins(coins)

for coin in coins:
    if coin == 0:
        tails += 1
    else:
        heads += 1
if tails == 0 or heads == 0:
    print("Nothing needs to be flipped")
elif tails == heads:
    print("It doesn't matter what to flip")
else:
    if tails > heads:
        need_flip = 'heads to tails'
    else:
        need_flip = 'tails to heads'
    print(f"Need to flip from {need_flip}")