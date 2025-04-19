hp = 100
def armor_set():
    pw = (hp * 5)/100
    pi = (hp * 10)/100
    pc = (hp * 15)/100
    pg = (hp * 18)/100
    x = 0
    while x != 1 or x != 2 or x!= 3:
        x = int(input('Escolha sua armadura: [1 - Armadura de madeira // 2 - Armadura de ferro // 3 - Armadura de cobre // 4 - Armadura de ouro]: '))
        if x == 1:
            print('Voce escolheu armadura de madeira.')
            print(f'Seu HP agora: {pw + hp}')
            exit()
        elif x == 2:
            print('Voce escolheu armadura de ferro.')
            print(f'Seu HP agora: {pi + hp}')
            exit()
        elif x == 3:
            print('Voce escolheu armadura de cobre.')
            print(F'Seu HP agora: {pc+hp}')
            exit()
        elif x == 4:
            print('Voce escolheu armadura de ouro.')
            print(f'Seu HP agora: {pg + hp}')
            exit()
armor_set()
