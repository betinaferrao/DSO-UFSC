from pedido_duplicado_exception import PedidoDuplicadoException
from pedido import Pedido


class ControladorPedidos():
    def __init__(self):
        self.__pedidos = []

    @property
    def pedidos(self):
        return self.__pedidos

    def busca_pedido_por_numero(self, numero):
        for pedido in self.__pedidos:
            if pedido.numero == numero:
                return pedido
        return None

    def incluir_pedido(self, pedido):
        if pedido in self.__pedidos:
            raise PedidoDuplicadoException
        if isinstance(pedido, Pedido):
            self.__pedidos.append(pedido)

    def excluir_pedido(self, numero):
        for pedido in self.__pedidos:
            if pedido.numero == numero:
                self.__pedidos.remove(pedido)
                return pedido
        return None

    def calcular_faturamento_pedidos(self, distancia, cpf):
        total = 0
        for pedido in self.__pedidos:
            if pedido.cliente.cpf == cpf:
                total += pedido.calcula_valor_pedido(distancia)
        return total

