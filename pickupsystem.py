import random
items = ['Touca de couro', 'Livro sobre combate', 'Espada de madeira (de treino)']
ritem = random.choice(items)
ritem2 = random.choice(items)
if ritem == ritem2:
    print(f'Voce encontra 2 {ritem} no chão!')
else:
    print(f'Voce encontra {ritem} e {ritem2} no chão!')
print('Oque deseja fazer?')
print('1 - pegar')
print('2 - analisar')
print('3 - ignorar')
act = int(input('Digite sua ação: '))
while act == 2:
    print('Voce analisa os itens, não parecem especiais...')
    act = int(input('Digite sua ação: '))
if act == 1:
    print(f'Voce pega {ritem}, {ritem2}')

elif act == 3:
    print('Voce ignora e volta para sua jornada.')
    exit()
else:
    print('...')
    exit()
n = int(input("Digite 1 para abrir sua bolsa: "))
if n == 1:
    if act == 1:
        print('-='*8)
        if ritem == ritem2:
            print(f'2x {ritem}')
            print('-=' * 8)
        else:
            print(f'1x{ritem2}')
            print(f'1x{ritem}')
            print('-=' * 8)
    elif act == 2 or act == 3:
        print('Voce não tem nada na bolsa.')
        exit()
exit()
