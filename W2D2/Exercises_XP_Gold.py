from random import randint as r

def throw_dice():
    return r(1,6)

def throw_until_doubles():
    dice = (throw_dice(), throw_dice())
    times = 0
    while dice[0] != dice[1]:
        dice = (throw_dice(), throw_dice())
        times += 1
    return times

def main():
    doubles = []
    for i in range(100):
        doubles.append(throw_until_doubles())
    return f'Total throws: {sum(doubles)}.\n Average throws to reach doubles: {sum(doubles)/len(doubles)}'

print(main())