import random
from collections import OrderedDict
from random import randint


class Jogo:

    NAIPES: str = '♠ ♡ ♢ ♣'.split()
    CARTAS: str = 'A 2 3 4 5 6 7 8 9 10 J Q K A'.split()
    vinte_um: int = 21
    pontuacao: int = 0
    begin: bool = True
    banqueiro: int = 0

    def __init__(self) -> None:
        pass

    @staticmethod
    def baralho() -> OrderedDict:

        baralho_aleatorio = [f'{c}{n}' for n in Jogo.NAIPES for c in Jogo.CARTAS]
        random.shuffle(baralho_aleatorio)
        baralho_dic = {}
        for v in baralho_aleatorio:
            if v[0] == 'A':
                baralho_dic[v] = 1
            if v[0] == '2':
                baralho_dic[v] = 2
            if v[0] == '3':
                baralho_dic[v] = 3
            if v[0] == '4':
                baralho_dic[v] = 4
            if v[0] == '5':
                baralho_dic[v] = 5
            if v[0] == '6':
                baralho_dic[v] = 6
            if v[0] == '7':
                baralho_dic[v] = 7
            if v[0] == '8':
                baralho_dic[v] = 8
            if v[0] == '9':
                baralho_dic[v] = 9
            if v[0] == '10':
                baralho_dic[v] = 10
            if v[0] == 'J':
                baralho_dic[v] = 10
            if v[0] == 'Q':
                baralho_dic[v] = 10
            if v[0] == 'K':
                baralho_dic[v] = 10
        return OrderedDict(baralho_dic)

    @staticmethod
    def vinte_um_calc(v: int) -> bool:
        Jogo.pontuacao += int(v)
        if Jogo.pontuacao == Jogo.vinte_um:
            print('Você conseguiu um 21')
            Jogo.begin = False
            return Jogo.begin
        elif Jogo.pontuacao > Jogo.vinte_um:
            print(f'Você perdeu porque passou de 21')
            Jogo.begin = False
            return Jogo.begin
        else:
            print(f'Voce tem {Jogo.pontuacao}')

    @staticmethod
    def retirar_carta(baralho: OrderedDict) -> tuple:
        return baralho.popitem()

    @staticmethod
    def passar_carta(carta: tuple, baralho: OrderedDict) -> None:
        baralho.update({carta[0]: carta[1]})
        baralho.move_to_end(f'{carta[0]}', last=False)

    @staticmethod
    def mao_banqueiro():
        Jogo.banqueiro += randint(1, 22)
        return Jogo.banqueiro

    @staticmethod
    def analise():
        print(f'Sua mão:{Jogo.pontuacao} \n Mão do Banqueiro: {Jogo.banqueiro}')
        if Jogo.pontuacao > Jogo.mao_banqueiro():
            print('Voce ganhou do banqueiro!')
        elif Jogo.pontuacao == Jogo.mao_banqueiro():
            print('O valor da mão do banqueiro é igual a sua, jogo empatado')
        elif Jogo.pontuacao < Jogo.mao_banqueiro():
            print('A mão do banqueiro chegou mais perto do 21, vc perdeu!')










