#status = 12
print('-='*6)
print('Aqui temos os Status para deixar seu personagem mais forte!')
print('-='*6)

print('''Voce tem exatamente 12 pontos para distribuir:
[ força ] - 1
[ agilidade ] - 1
[ destreza ] - 1
[ intelecto ] - 1''')
print('Vamos começar colocando seus pontos em força! ')
strenght = int(input('Força: '))
if strenght > 12:
    print('Ops, voce não pode adicionar mais que 12 pontos de status! tente novamente.')
    exit()
elif strenght < 0:
    print('Ops, voce não pode adicionar menos que 0 pontos de status! tente novamente.')
    exit()
elif strenght  == 12:
    print('Voce usou todos seus pontos em força...')
    print('Seu desenvolvimento de status finalizou.')
    exit()
else:
    print(f"adicionado {strenght} pontos de força para seus status!")
remain = 12 - strenght
print(f'Ok! Agora vamos para os status de agilidade! Voce tem {remain} pontos para gastar! ')

agil = int(input('Agilidade: '))
remainagil = remain - agil
if remainagil == 0:
    print('Acabou seus pontos de desenvolvimento de personagem.')
    exit()
if agil > remain:
    print('Ops, voce não pode adicionar mais que 12 pontos de status! tente novamente.')
    exit()
elif agil < 0:
    print('Ops, voce não pode adicionar menos que 0 pontos de status! tente novamente.')
    exit()

else:
    print(f"adicionado {agil} pontos de agilidade para seus status!")
agilremain = remain - agil
if remain == 0:
    print("Voce já gastou todos seus pontos de status!")
    exit()
elif remain < 0:
    print("Houve um erro, voce está com pontos negativos!")
elif remain < 2:
    print("Voce tem poucos pontos para gastar!")
elif remain >= 3:
    print(f"Voce tem {agilremain} pontos para gastar em seus status!")
    xrk1 = int(input('Digite 1 para continuar '))
    if xrk1 == 1:
        print('Vamos para a "Destreza agora!"')
    else:
        print('...')
        exit()
print(f'''Seus status agora são:
[força] - {strenght + 
           1}
[agilidade] - {agil + 
               1}
[destreza] - A ser decidido.
[intelecto] - A ser decidido.''')
DEX = int(input('Digite o valor de status de sua destreza aqui: '))
dexremain = agilremain - DEX
if dexremain == 0:
    print('Acabou seus pontos para distribuir!')
    exit()
elif dexremain < 0:
    print('Houve um erro, seus pontos estão negativos.')
    exit()
elif dexremain < 2:
    print(f'Voce tem poucos pontos para distribuir! ({dexremain})')
elif dexremain >= 2:
    print(f'Voce tem {dexremain} pontos para distribuir!')
else:
    print('...')
    exit()
print('Ok, agora vamos para o ultimo status, intelecto!')
print(f'''Seus status estão assim até agora:
[força] - {strenght + 
           1}
[agilidade] - {agil + 
               1}
[destreza] - {DEX + 
              1}
[intelecto] - A ser decidido.''')
intel = int(input('Digite seu intelecto aqui: '))
intelremain = dexremain - intel
if  intelremain > 0:
    print('Voce não gastou todos os pontos! Não se preocupe, voce pode fazer isto de novo mais tarde.')
elif intelremain == 0:
    print('Voce gastou todos seus pontos, podemos voltar a aventura!')

else:
    print('...')
    exit()
print(f'''Seus status agora são:
[força] - {strenght +1}
[agilidade] - {agil +1}
[destreza] - {DEX +1}
[intelecto] - {intel +1}''')
exit()
#"""""Complete"""""
