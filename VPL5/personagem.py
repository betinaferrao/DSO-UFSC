
from enum import Enum

from abstractPersonagem import AbstractPersonagem


class Tipo(Enum):
    agua = 0
    terra = 1
    ar = 2
    fogo = 3


class Personagem(AbstractPersonagem):
    def __init__(self, tipo: Tipo, energia, habilidade, velocidade, resistencia):
        self.__tipo = tipo
        self.__energia = energia
        self.__habilidade = habilidade
        self.__velocidade = velocidade
        self.__resistencia = resistencia

    @property
    def tipo(self) -> Tipo:
        return self.__tipo


    @property
    def energia(self) -> int:
        return self.__energia


    @property
    def habilidade(self) -> int:
        return self.__habilidade


    @property
    def velocidade(self) -> int:
        return self.__velocidade


    @property
    def resistencia(self) -> int:
        return self.__resistencia
