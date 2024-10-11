time = 2
cdmg_kindzu = 15
newcmdgkindzu = cdmg_kindzu + (15 * 50)/100
# 0 = Morning // 1 = Late // 2 = Night
def timeset():
    if time == 2:
        print('Está de noite.')
        cdmg_kindzu = newcmdgkindzu
        print(f'O dano da criatura kindzu agora é {newcmdgkindzu}')
timeset()
