class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho

    @property
    def alto(self):
       # print('Llamando método get nombre')
        return self._alto

    @alto.setter
    def alto(self, alto):
       # print('Llamando método set nombre')
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    def __str__(self):
        return f'Alto:' + str(self._alto) + ' Ancho:' + str(self._ancho)





# figura = FiguraGeometrica(5, 5)
# print(figura)