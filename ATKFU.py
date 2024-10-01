import random
l = [1, 1, 2, 2, 2]
x = random.choice(l)
def atk():
    if x == 2:
        return 'Atacado.'
    else:
        return 'Não atacado.'
print(atk())
