
from controladorJogo import ControladorJogo
from personagem import Personagem
from carta import Carta
print('oi')
controlador = ControladorJogo()
p1 = Personagem(1, 2, 3, 4, 5)
c1 = Carta(p1)

print(c1.valor_total_carta())
# print(controlador.jogada())