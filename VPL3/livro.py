from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numero_capitulo: int, titulo_capitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = [autor]
        self.__capitulos = [Capitulo(numero_capitulo, titulo_capitulo)]
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        self.__ano = ano
    
    @property
    def editora(self):
        return self.__editora
    
    @editora.setter
    def editora(self, editora):
        self.__editora = editora

    @property
    def autores(self):
        return self.__autores
    
    def incluir_autor(self, autor: Autor):
        if type(autor) is Autor:
            if autor not in self.__autores:
                self.__autores.append(autor)
        
    def excluir_autor(self, autor: Autor):
        if autor in self.__autores:
            self.__autores.remove(autor)

    def incluir_capitulo(self, numeroCapitulo: int, tituloCapitulo: str):
        repetido = False
        for i in range(0,len(self.__capitulos)):
            if self.__capitulos[i].numero == numeroCapitulo:
                repetido =True
        if not repetido:
            capi = Capitulo(numeroCapitulo, tituloCapitulo)
            self.__capitulos.append(capi)

    def excluir_capitulo(self, tituloCapitulo: str):
        for i in self.__capitulos:
            if i.titulo == tituloCapitulo:
                self.__capitulos.remove(i)
    
    def find_capitulo_by_titulo(self, tituloCapitulo: str):
        for i in self.__capitulos:
            if i.titulo == tituloCapitulo:
                return i
