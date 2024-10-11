#Wood armor kit +5% HP
#Iron armor kit +10% HP
#Cooper armor kit +15% HP
hp = 100
pW = (hp * 5)/100
pI = (hp * 10)/100
pC = (hp * 15)/100
x = 0
while x != 1 or x != 2 or x!= 3:
    x = int(input('Escolha sua armadura: [1 - Armadura de madeira // 2 - Armadura de ferro // 3 - Armadura de cobre]: '))
    if x == 1:
        print('Voce escolheu armadura de madeira.')
        print(f'Seu HP agora: {pW + hp}')
        exit()
    elif x == 2:
        print('Voce escolheu armadura de ferro.')
        print(f'Seu HP agora: {pI + hp}')
        exit()
    elif x == 3:
        print('Voce escolheu armadura de cobre.')
        print(F'Seu HP agora: {pC+hp}')
        exit()
