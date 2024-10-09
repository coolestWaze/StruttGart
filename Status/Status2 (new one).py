#status = 12
print('-='*6)
print('Aqui temos os Status para deixar seu personagem mais forte!')
print('-='*6)

print('''Voce tem exatamente 12 pontos para distribuir:
[ força ] - 1
[ agilidade ] - 1
[ destreza ] - 1
[ intelecto ] - 1''')
def upddmg(strenght):
    return 10 + strenght
def updhp(dex):
    return 5 + dex + hp
dmg = 10
hp = 100
pontos = 12
print('Vamos começar com os pontos em força! ')
strenght = int(input('Coloque os pontos em força aqui: '))
truedmg = upddmg(strenght)
if strenght > pontos:
    print('Voce não possui pontos de status suficiente.')
    exit()
elif strenght < 0:
    print('Voce não pode adicionar pontos negativos.')
    exit()
else:
    print(f'{strenght} pontos adicionados!')
    pontos -= strenght
    print(f'Voce tem agora {pontos} pontos para gastar.')
    if pontos == 0:
        print('Voce gastou todos os pontos.')
        exit()
    print(f'Seu dano agora é {truedmg}')
print('Otimo, agora vamos para agilidade!')
agility = int(input('Coloque os pontos em agilidade aqui: '))
if agility > pontos:
    print('Voce não possui pontos suficiente.')
    exit()
elif agility < 0:
    print('Voce não pode adicionar pontos negativos.')
    exit()
else:
    print(f'{agility} pontos adicionados.')
    pontos -= agility
    if pontos == 0:
        print('Voce gastou todos os pontos.')
        exit()
    else:
        print(f'Voce tem agora {pontos} pontos para gastar.')
print('Destreza agora!')
dex = int(input('Coloque os pontos em destreza aqui: '))
if dex > pontos:
    print('Voce não possui pontos suficiente.')
    exit()
elif dex < 0:
    print('Voce não pode adicionar pontos negativos.')
    exit()
else:
    print(f'{dex} pontos adicionados.')
    pontos -= dex
    if pontos == 0:
        print('Acabou seus pontos.')
        print(f'Voce tem agora {dex} pontos para gastar.')
        print(f'seu hp agora é: {updhp(dex)}')
        exit()
    else:
        print(f'Voce tem agora {pontos} pontos para gastar.')
        print(f'seu hp agora é: {updhp(dex)}')
print('E por ultimo, intelecto: ')
intel = int(input('Digite seu intelecto aqui: '))
if pontos == 0:
    print('Voce gastou todos os pontos.')
elif intel > pontos:
    print('Voce não possui pontos suficiente.')
elif intel < 0:
    print('Voce não pode adicionar pontos negativos.')
    exit()
else:
    pontos -= intel
    if pontos == 0:
        print('Voce usou todos seus pontos nesta personalização de status!')
        exit()
    elif pontos >= 1:
        print(f'ainda te restam {pontos} pontos, não se preocupe, futuramente voce poderá gasta-los.')
        exit()
