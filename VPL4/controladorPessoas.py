from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico

class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__listaClientes = []
        self.__listaTecnicos = []
	
    @property
    def clientes(self):
        return self.__listaClientes
    
    @property
    def tecnicos(self):
        return self.__listaTecnicos

    def inclui_cliente(self, codigo :int, nome :str):
        incluido = False
        for i in self.__listaClientes:
            if i.codigo == codigo:
                 incluido = True
        if not incluido:
            cliente = Cliente(nome, codigo)
            self.__listaClientes.append(cliente)
            return cliente

    def inclui_tecnico(self, codigo :int, nome :str):
        incluido = False
        for i in self.__listaTecnicos:
            if i.codigo == codigo:
                 incluido = True
        if not incluido:
            tecnico = Tecnico(nome, codigo)
            self.__listaTecnicos.append(tecnico)
            return tecnico