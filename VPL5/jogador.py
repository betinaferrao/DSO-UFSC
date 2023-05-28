


from abstractJogador import AbstractJogador
from carta import Carta
import random


class Jogador(AbstractJogador):
    def __init__(self, nome):
        self.__nome = nome
        self.__cartas = [Carta]


    @property
    def nome(self) -> str:
        return self.__nome


    def baixa_carta_da_mao(self):
        carta = random.choice(self.__cartas)
        self.__cartas.remove(carta)
        return carta


    @property
    def mao(self) -> list:
        return self.__cartas


    def inclui_carta_na_mao(self, carta: Carta):
        if isinstance(carta, Carta):
            self.__cartas.append(carta)
