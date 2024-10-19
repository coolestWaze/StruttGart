import random
import time
fish = ['Peixe comum', 'Salmão']
print('Voce está nas margens de um rio.')
fishing = int(input('deseja pescar? [1 para confirmar] - '))
if fishing != 1:
    print('Voce não pesca.')
    exit()
else:
    print('Voce decide pescar. (para encontrar um peixe deve levar alguns segundos...)')
    tempo = random.randint(2, 15)
    time.sleep(tempo)
    print('Voce encontrou um peixe!', end='')
    getfish = int(input(' Digite 1 para tentar pesca-lo: '))
    if getfish != 1:
        print('Voce não pesca o peixe.')
        exit()
    else:
        pickfish = random.randint(1, 20)
        if pickfish < 10:
            print('Voce não consegue pescar o peixe.')
        elif pickfish >= 10:
            x = random.choice(fish)
            print('Voce pesca o peixe!')
            print(f'Voce pega um: {x}!')
            if x == 'Salmão':
                print('Parabéns! voce pegou um peixe incomum!')
            else:
                print('Voce pegou um peixe comum.')
                exit()
exit()
