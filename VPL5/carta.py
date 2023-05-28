


from abstractCarta import AbstractCarta
from personagem import Personagem


class Carta(AbstractCarta):
    def __init__(self, personagem: Personagem):
        self.__personagem = personagem


    def valor_total_carta(self) -> int:
        total = self.personagem.tipo + self.__personagem.energia + self.__personagem.habilidade + self.__personagem.resistencia + self.__personagem.velocidade
        return total


    @property
    def personagem(self) -> Personagem:
        return self.__personagem
