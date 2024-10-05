import random
hpm = 30
miss = [1, 1, 2]
p = random.choice(miss)
def fungi():
    if p == 1:
        global hpm
        z = random.randint(5, 30)
        print('Voce acertou.')
        print(f'Dano: {z}')
        hpm -= z
    else:
        print('Voce errou.')
def hyoto_1():
    x = random.choice(miss)
    if p == 1:
        global hpm
        z1 = random.randint(8, 28)
        print('Voce acertou.')
        print(f'Dano: {z1}')
        hpm -= z1
x = int(input('digite 1 para fungi e 2 para hyoto: '))
if x == 1:
    fungi()
    exit()
elif x == 2:
    hyoto_1()
    exit()
