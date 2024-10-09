import random
miss = [1, 2, 2]
hpm = 45
def __fungi__():
    global hpm
    dmgf = random.randint(1, 30)
    r = random.choice(miss)
    if r == 1:
        print('Voce erra')
    elif r == 2:
        print('Voce acerta!')
        print(f'Voce da {dmgf} de dano!')
        hpm -= dmgf
        print(f'HP da criatura: {hpm}')
def __hyoto__():
    global hpm
    dmgh = random.randint(5, 25)
    r = random.choice(miss)
    if r == 1:
        print('Voce erra.')
    elif r == 2:
        print('Voce acerta!')
        print(f'Voce da {dmgh} de dano!')
        hpm -= dmgh
        print(f'HP da criatura: {hpm}')

while hpm > 0:
    act = int(input('Digite 1 para "Fungi" e 2 para "Hyoto": '))
    if act == 1:
        __fungi__()
    elif act == 2:
        __hyoto__()
    if hpm <= 0:
        print('Voce derrotou a criatura!')
        exit()
