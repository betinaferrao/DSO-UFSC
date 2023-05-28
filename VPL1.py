class Ordenacao():

    def __init__(self, array_para_ordenar: list):
        self.array_para_ordenar = array_para_ordenar

    def ordena(self):
        elementos = len(self.array_para_ordenar)-1
        ordenado = False
        while not ordenado:
            ordenado = True
            for i in range(elementos):
              if self.array_para_ordenar[i] > self.array_para_ordenar[i+1]:
                   self.array_para_ordenar[i], self.array_para_ordenar[i+1] = self.array_para_ordenar[i+1],self.array_para_ordenar[i]
                   ordenado = False
        return self.array_para_ordenar
        

    def toString(self):
        string = ""
        for index, elem in enumerate(self.array_para_ordenar):
            if index == len(self.array_para_ordenar)-1:
                string += str(elem)
            else:
                string += str(elem) + ","
        return string