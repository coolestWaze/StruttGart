#Wood armor kit +5% HP
#Iron armor kit +10% HP
#Cooper armor kit +15% HP
hp = 100
pW = (hp * 5)/100
pI = (hp * 10)/100
pC = (hp * 15)/100
x = 0
while x != 1 or x != 2 or x!= 3:
    x = int(input('Choose your armor [1 - Wood armor // 2 - Iron armor // 3 - Cooper armor]: '))
    if x == 1:
        print('You choose wood armor.')
        print(f'Your HP now: {pW + hp}')
        exit()
    elif x == 2:
        print('You choose Iron armor.')
        print(f'Your HP now: {pI + hp}')
        exit()
    elif x == 3:
        print('You choose Cooper armor.')
        print(F'Your HP now: {pC+hp}')
        exit()
