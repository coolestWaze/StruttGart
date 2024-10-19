inv = ['Salmão cru']
dmgedhp = 50
print(f'Voce está com a metade da vida ({dmgedhp})! Coma oque tem para recupar o HP.')
print(f'Seu inventário: {inv}')
eat = int(input(f'Deseja comer {inv[0]}? [1 para confirmar?] - '))
if eat != 1:
    print(f'Voce não come {inv[0]}.')
else:
    print(f'Voce come!')
    dmgedhp += 25
print(f'Voce está com {dmgedhp} de vida agora.')
