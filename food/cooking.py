import random
print('Voce está em frente ao fogão.')
food = ['Pão']
x = 5
while x > 1:
    x = int(input('Digite 0 para sair e 1 para continuar: '))
    if x == 0:
        print('Voce sai de frente do fogão.')
        exit()
    elif x > 1:
        print('...')
    elif x == 1:
        print('Voce continua.')
        print('Oque deseja fazer?')
        K = str(input(f'Opções: {food}').lower().strip())
        if K == 'pao':
            print(f'Voce tenta preparar pão.')
            dado = random.randint(1, 20)
            if dado <= 10:
                print(f'Voce não consegue fazer um bom pão. (dado: {dado})')
            else:
                print(f'Voce consegue fazer um bom pão (dado: {dado}).')
eat = int(input(f'Deseja comer {food[0]}? (1 para confirmar)'))
if eat == 1:
    print('Voce come.')

xg = random.randint(0, 20)
if xg > 10:
    print(f'+12 HP (dado = {xg})')
elif xg <= 10:
    print(f'+6 HP (dado = {xg})')

# it absolutelly sucks, nvm, i'll fix this tomorrow. (29/10/24, Brazil)
