import random
import time

hp = 100
print('[?] - Olá aventureiro! Como vai? Está pronto para entrar nas ruínas de StruttGart? Espero que sim!')
print('[?] - Vamos começar do Básico, me conte seu nome?')
player = input('Digite seu nome aqui: ')
print(f"''{player}''... Ok! entendido. Agora vamos para algo mais interessante, ARMAS! Vamos lá!")
print(f'''ok, {player}, escolha um número para adquirir alguma dessas armas: 
Espada curta
Espada média
Espada longa
Faixa para punho
Núcleo mágico''')
arma = str(input('Escolha aqui: ')).strip().lower()
if arma == 'espada curta':
    print('[?] - Aham, voce parece ser bem agil, boa escolha!')

elif arma == 'espada media' or arma == 'espada média':
    print('Básico, arma média é algo que da certo com todos, voce vai se acostumar!')

elif arma == 'espada longa':
    print('[?] - Wow... Voce tem que ser bem forte para usar esta arma\nmas tenho certeza que vai se acostumar!')

elif arma == 'faixa para punho':
    print('[?] - Entendi, então voce gosta de sair na mão com os outros? interessante...')

elif arma == 'nucleo magico' or arma == 'núcleo mágico' or arma == 'núcleo magico' or arma == 'nucleo mágico':
    print('[?] - Faz tempo que não vejo aventureiros escolherem isto...')

else:
    print('Ops, houve um erro, talvez tenha digitado errado?')
    exit()

print('[?] - Certo, agora eu me despeço de voce por enquanto, a criação de personagem ainda não terminou!')
xk = int(input('Digite 1 para continuar '))
if xk == 1:
    print('[?] - Agora irei chamar o grande mestre Fuingett, ele irá dar continuação a sua aventura! A propósito, ')
    print('Eu nem me apresentei, prazer, sou Meya, a assistente de aventureiros aqui em StruttGart!')
    xk1 = int(input('Digite 1 para continuar '))
    print('[Meya] - Agora vamos chamar Fuingett, temos que contar até 3 e bater uma palma,', end=' ')
    print('faça isso comigo.')
else:
    print('...')
    (exit())
xk2 = int(input('digite 1 para continuar'))
if xk2 == 1:
    print('...')
    time.sleep(1)
    print('1')
    time.sleep(2)
    print('2')
    time.sleep(2)
    print('3')
    time.sleep(2)
    print('E agora..')
    time.sleep(1.5)
    print('*clap*')
else:
    print('...')
    exit()
print('*Mestre Fuingett aparece, com um semblante assustador e misterioso...*')
xk3 = int(input('digite 1 para continuar '))
if xk3 == 1:
    print('[Fuingett] - Oh.. Este é o novo aventureiro de StruttGart..? Venha comigo rapaz')
else:
    print('...')
    (exit())
print('''Ir com Fuingett: [1]
Perguntar sobre quem é ele: [2]''')
resposta = int(input('Digite sua resposta: '))
if resposta == 1:
    print(f'[{player}] - claro.. *Vai atrás de Fuingett*')
elif resposta == 2:
    print(f'[{player}] - Senhor, mas.. quem é voce?')
    print('[Fuingett] - Olha garoto, não precisa me chamar de senhor, haha!')
    time.sleep(0.2)
    print('Eu sou Fuingett, o mago de StruttGart, não se preocupe, ao longo de sua jornada voce irá aprender')
    print('Mais sobre esta terra lendária e sobre mim.')
    time.sleep(0.2)
    print(f'[{player}] - ok.. *Vai atrás de Fuingett*')
xk4 = int(input('digite 1 para continuar '))
if xk4 == 1:
    print('*Voce segue para uma caverna escura onde Fuingett te leva...')
else:
    print('...')
    (exit())
print('*Andando por caminhos no interior da caverna* [Fuingett] - Aqui estamos, sem a iluminação do sol, eu posso')
print('alterar sua raça, que atualmente é desconhecida.')
print('*Fuingett puxa um papel dos bolsos e te apresenta, neste papel esta: *')
print('''[ 1 ] - Humano
[ 2 ] - Hobbit
[ 3 ] - Anão
[ 4 ] - Gigante
[ 5 ] - Strovin''')
raca = int(input('Escolha sua raça: '))
if raca == 1:
    print('Voce escolheu Humano!')
elif raca == 2:
    print('Voce escolheu Hobbit!')
elif raca == 3:
    print('Voce escolheu Anão!')
elif raca == 4:
    print('Voce escolheu Gigante!')
elif raca == 5:
    print('Não me lembro de ter deixado isto aqui, porfavor, escolha outra raça.')
    while raca == 5:
        raca = int(input('Escolha sua raça: '))
        if raca == 5:
            print('...')
if raca > 5 or raca < 0:
    print('...')
    exit()
print('[Fuingett] - Ótimo, podemos continuar!')
xk5 = int(input('Digite 1 para continuar '))
while xk5 != 1:
    print('...')
    xk5 = int(input('Digite 1 para continuar '))
    if xk5 != 1:
        print('...')
if xk5 == 1:
    print('Vamos lá, vamos voltar para a superficie de StruttGart!')
time.sleep(0.2)
print('*de volta a superficie, voce sente algo correndo por suas veias...')
if raca == 1:
    print('Voce tem um sangue bem... humano?')
elif raca == 2:
    print('voce se sente pequeno... e com fome')
elif raca == 3:
    print('voce se sente pequeno...')
elif raca == 4:
    print('voce se sente grande, e pesado...')
print('*Saindo das cavernas, voce ve criaturas pelos céus, até que uma se aproxima de forma assustadora...')
print('[Fuingett] - Aqui estamos, seu primeiro combate pode iniciar agora, não tenho muito que explicar garoto,')
print('apenas derrote-o, é um experimento. ')
print('''Opções: [ 1 ] - "Fuingett, eu não posso, eu não entendo oque estou fazendo..."
[ 2 ] - ... *Vai para cima da criatura*''')
opc = int(input('Escolha oque fará: '))
while opc != 2 and opc != 1:
    print('...')
    opc = int(input('Escolha oque fará: '))
    if opc != 2 and opc != 1:
        print('...')
if opc == 2:
    print("[Fuingett] - Aham.. voce é rápido. Boa sorte!")
elif opc == 1:
    print("[Fuingett] - Voce está pronto garoto, se acalme, nada vai dar errado.")
    print("Opções: [ 1 ] - *Continue, e enfrente a criatura*"
            "[ 2 ] - *Peça peça para entender melhor sobre*")
    opc1 = int(input('Escolha sua ação: '))
    if opc1 == 2:
        print('[Fuingett] - Não há oque entender, apenas vá.')
    elif opc == 1:
        print('Voce enfrenta seu medo e vai...')
atk = random.randint(1, 20)
atkd = random.randint(5, 25)
atkdc = random.randint(5, 15)
defesa = random.randint(1, 20)
esquiva = random.randint(1, 20)
atkmiss = random.randint(1, 20)
print('''Voce deseja:   [ 1 ] - contra-atacar
                    [ 2 ] - defender
                    [ 3 ] - esquivar''')
esc = int(input('Digite sua ação: '))
if esc == 1:
    print('Voce tenta contra-atacar! ')
    print(atk)
    if atk > 10:
        print('Voce acerta!')
        print(atkd)
        print(f'Voce contra-ataca e da {atkd} de dano!')

    elif atk <= 10:
        print('Voce erra e receberá outro ataque.')
        print(atkd)
        hp -= atkd
        print(f'voce é atacado e sofre {atkd} de dano.')
        print(f'Voce está com {hp} de vida.')
        if hp <= 0:
            print('...')
            time.sleep(1)
            print('Voce morreu... Tente novamente.')
            exit()
elif esc == 2:
    print('Voce tenta se defender')
    print(defesa)
    if defesa > 8:
        print('Voce defende!')
    elif defesa <= 8:
        print('Voce não se defende')
        print(atkd)
        print(f'Voce sofrerá {atkd} de dano!')
        hp -= atkd
        print(f'Voce está com {hp} de vida.')
        if hp <= 0:
            print('...')
            time.sleep(1)
            print('Voce morreu, tente novamente.')
            exit()
elif esc == 3:
    print('Voce tenta esquivar.')
    print(esquiva)
    if esquiva > 10:
        print('Voce esquiva!')
    elif esquiva <= 10:
        print('Voce não esquiva.')
        print(atkd)
        print('Voce sofrerá {atkd} de dano.')
        hp -= atkd
        print(f'Voce está com {hp} de vida.')
        if hp <= 0:
            print('...')
            time.sleep(1)
            print('Voce morreu, tente novamente.')
            exit()
print('Ótimo, chegou a hora de atacar! ')
print(f'''Oque deseja fazer? 
[ 1 ] ataque básico de {arma}''')
kl = int(input('Digite sua ação: '))
hpc = 30
while kl != 1:
    print('...')
    kl = int(input('Digite sua ação: '))
    if kl != 1:
        print('...')
else:
    print('Voce tenta atacar!')
    print(atkmiss)
    if atkmiss > 10:
        print('Voce acerta!')
        print(atkd)
        print(f'Voce da {atkd} de dano!')
        if atkd > 15:
            print('A criatura parece muito ferida!')
        elif atkd >= 10:
            print('A criatura parece ferida!')
        else:
            print('A criatura não parece ter tido uma reação sob seu ataque.')
    elif atkmiss <= 10:
        print('Voce erra.')
        print('Voce será atacado. ')
        print(atkdc)
        print(f'Voce tomou {atkdc} de dano.')
        hp -= atkdc
        if hp <= 0:
            print('Voce morreu... Tente novamente.')
            exit()
print('Voce será atacado. ')
print(atkdc)
print(f'Voce tomou {atkdc} de dano.')
hp -= atkd
if hp <= 0:
    print('Voce morreu... Tente novamente.')
    exit()
else:
    print('Voce pode atacar agora! ')
print(f'''Oque deseja fazer? 
[ 1 ] ataque básico de {arma}''')
kl1 = int(input('Digite sua ação: '))
while kl1 != 1:
    print('...')
    kl1 = int(input('Digite sua ação: '))
    if kl1 != 1:
        print('...')
else:
    print('Voce tenta atacar a criatura.')
    print(atkmiss)
    if atkmiss > 10:
        print('Voce acerta.')
        print(atkd)
        print(f'Voce deu {atkd} de dano na criatura.')
        hpc -= atkd
        if hpc == 0:
            print('Voce derrotou a criatura! ')
            print('+Núcleo de Vingarr')
        else:
            print('A criatura parece assustada, após seus breves ataques, ela foge.')
            print('+Núcleo de Vingarr')
    if atkmiss <= 10:
        print('Voce erra, porém com a tentativa de ataque, a criatura foge assustada.')
        print('+Núcleo de Vingarr')
print('[ Fuingett ] - Hah, como esperado, voce derrotou a criatura com facilidade...')
print('Pelo jeito, também ganhou algo né? "Núcleo de Vingarr" é como se chama isto, é realmente útil, voce pode troca-lo', end=' ')
print('por XP no centro de StruttGart.')
print('Podemos continuar, vamos conhecer os moradores de StruttGart.')

#NOT FINISHED YET
