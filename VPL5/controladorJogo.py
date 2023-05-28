from abc import ABC, abstractmethod
from carta import *
from personagem import *
from jogador import *
from mesa import *
from abstractControladorJogo import AbstractControladorJogo


class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        self.__personagems = [Personagem]
        self.__baralho = [Carta]


    @property
    def personagems(self) -> list:
        return self.__personagems


    @property
    def baralho(self) -> list:
        return self.__baralho


    def inclui_personagem_na_lista(self, energia: int, habilidade: int,
                                velocidade: int, resistencia: int,
                                tipo: Tipo) -> Personagem:
        if type(tipo) is Tipo and isinstance(energia, int) and isinstance(habilidade, int) and isinstance(velocidade, int) and isinstance(resistencia, int):
            personagem = Personagem(tipo, energia, habilidade, velocidade, resistencia)
            self.__personagems.append(personagem)
            return personagem


    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        if isinstance(personagem, Personagem):
            carta = Carta(personagem)
            self.__baralho.append(carta)
            return carta

    def jogada(self, mesa: Mesa) -> Jogador:
        cartajog1 = mesa.carta_jogador1
        cartajog2 = mesa.carta_jogador2
        jog1 = mesa.jogador1
        jog2 = mesa.jogador2

        if (cartajog1.valor_total_carta() > cartajog2.valor_total_carta()):
            jog1.inclui_carta_na_mao(cartajog1)
            jog1.inclui_carta_na_mao(cartajog2)
        
        if(cartajog2.valor_total_carta() > cartajog1.valor_total_carta()):
            jog2.inclui_carta_na_mao(cartajog1)
            jog2.inclui_carta_na_mao(cartajog2)
        
        if (cartajog1.valor_total_carta() == cartajog2.valor_total_carta()):
            jog1.inclui_carta_na_mao(cartajog1)
            jog2.inclui_carta_na_mao(cartajog2)
        
        if len(mesa.jog1.mao) == 0:
            return jog2
        elif len(mesa.jog2.mao) == 0:
            return jog1
        else:
            return None
