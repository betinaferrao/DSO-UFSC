from cliente import Cliente
from tipo_pedido import TipoPedido
from item_pedido import ItemPedido
from cliente_fidelidade import ClienteFidelidade


class Pedido():
    def __init__(self, numero: int, cliente: Cliente, tipo: TipoPedido):
        self.__numero = numero
        self.__cliente = cliente
        self.__tipo = tipo
        self.__itens = []

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def itens(self):
        return self.__itens

    def inclui_item_pedido(self, codigo, descricao, preco):
        item = ItemPedido(codigo, descricao, preco)
        for item_pedido in self.__itens:
            if item_pedido.codigo == codigo:
                return None
        self.__itens.append(item)
        return item

    def exclui_item_pedido(self, codigo):
        for item_pedido in self.__itens:
            if item_pedido.codigo == codigo:
                self.__itens.remove(item_pedido)
                return item_pedido
        return None

    def calcula_valor_pedido(self, distancia: float):
        total = 0

        for item in self.__itens:
            total += item.preco_unitario
        total += self.__tipo.fator_distancia * distancia

        if isinstance(self.__cliente, ClienteFidelidade):
            total -= total * self.__cliente.desconto

        return total