import random

vida2 = 10
player1 = input('Digite seu nome: ')
# player2 = 'Torkh' #I'll not need this for now.
dice = random.randint(0, 21)
print(f'Olá {player1}, este é o teste do sistema de "save"')
print('Basicamente consiste em levantar outro NPC que esta prestes a morrer.')
n1 = int(input('Digite 1 para continuar '))
if n1 == 1:
    hpless = random.randint(11, 900)
    g = f'Oh não! Torkh acabou de receber um ataque, o dano tomado foi {hpless}'

    def caido():
        if totaldmg <= 0:
            return True
        else:
            return False

    totaldmg = vida2 - hpless
    x = caido()
else:
    print('...')
    exit()
if caido() == True:
    print('Ele caiu, tente ajuda-lo!')
else:
    print(f'Ele ainda está de pé! a vida do mesmo é de {totaldmg}')

help = int(input('Digite 1 para salva-lo, 2 para desistir. '))
if help == 1:
    print('Voce tenta ajuda-lo: ')
    print(dice)
    if dice > 10 and dice <= 15:
        print('Voce salva Torkh, ele está com 1 de HP agora!')
        print(f'[ Torkh ] - Estou me sentindo melhor. Obrigado {player1}')
    elif dice <= 10:
        print('''Voce não salva Torkh.''')
        print('[ Torkh ] - M-Mundo...')
    elif dice > 15:
        print('Voce salva Torkh com maestria! ele está com 5 de HP agora!')
    elif dice == 0:
        print('Oh não! Voce falhou completamente, voce não poderá salvar ninguém por 3 rodadas! ')

    else:
        print('...')
        exit()
elif help == 2:
    print('Voce desiste. Torkh morre na sua frente, implorando por sua ajuda.')
