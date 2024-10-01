import random
player = input('Digite seu nome: ')
hp = 100
print('Voce tem 100 de vida! ')
atk = ['stab']
atkr = random.choice(atk)
atkf = random.randint(100, 100)
defesa = [1, 2, 1, 2]
defesar = random.choice(defesa)
print(atkr)
if atkr == 'stab':
    print("Voce foi perfurado, oque deseja fazer?")
    print("[ 1 ] - defender")
    act = int(input('Digite sua ação: '))
    if act == 1:
        print('Voce tenta defender; ')
        print(defesar)
        if defesar == 1:
            print('Voce se defende!')
        else:
            print('Voce não se defende! ')
            print(f"voce recebe {atkf} de dano")
            hp -= atkf
            print(f'Voce tem agora {hp} de vida.')
            if hp <= 0:
                print('Voce morreu.')
                exit()
    else:
        print('...')
        exit()
print('Voce será atacado denovo!')
print(atkr)
if atkr == 'stab':
    print("Voce foi perfurado, oque deseja fazer?")
    print("[ 1 ] - defender")
    act = int(input('Digite sua ação: '))
    if act == 1:
        print('Voce tenta defender; ')
        print(defesar)
        if defesar == 1:
            print('Voce se defende!')
        else:
            print('Voce não se defende! ')
            print(f"voce recebe {atkf} de dano")
            hp -= atkf
            print(f'Voce tem agora {hp} de vida.')
            print(hp)
            if hp <= 0:
                print('Voce morreu.')
                exit()
print('Voce será atacado denovo!')
print(atkr)
if atkr == 'stab':
    print("Voce foi perfurado, oque deseja fazer?")
    print("[ 1 ] - defender")
    act = int(input('Digite sua ação: '))
    if act == 1:
        print('Voce tenta defender; ')
        print(defesar)
        if defesar == 1:
            print('Voce se defende!')
        else:
            print('Voce não se defende! ')
            print(f"voce recebe {atkf} de dano")
            hp -= atkf
            print(f'Voce tem agora {hp} de vida.')
            if hp <= 0:
                print('Voce morreu.')
                exit()

# I REMOVED SOME ATTACKS.
# THE MIN AND MAX DAMAGE MUST BE CHANGED, THIS IS JUST FOR A EXPERIMENT!!!
