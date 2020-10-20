from main import Jogo
from collections import OrderedDict


def jogar():

    Jogo.mao_banqueiro()
    # print(players.jogadores)
    vinte_um = Jogo.baralho()
    # print(vinte_um)
    # print(tuple(vinte_um))
    while Jogo.begin:
        guess = input('Escolha "carta" para pega-la, "passar" para move-la para o final, '
                      'e "fim" para encerrar o jogo com cartas que tem').strip()
        if guess == 'carta':
            carta1 = Jogo.retirar_carta(vinte_um)
            print(f'Sua carta é: {carta1}')
            Jogo.vinte_um_calc(carta1[1])

        elif guess == 'passar':
            carta_b = Jogo.retirar_carta(vinte_um)
            Jogo.passar_carta(carta_b, vinte_um)

        elif guess == 'fim':
            Jogo.analise()
            break
        else:
            print('Palavra invalida')


jogar()


