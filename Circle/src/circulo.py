class Circulo:
    def __init__(self, x, y, raio):
        # definir coordenadas positivas
        if x < 0 or y < 0:
            raise ValueError(" As coordenadas devem ser no valor maior que zero.")
        if raio < 0:
            raise ValueError(" O raio precisa ser maior que zero")

        self._x = x
        self._y = y
        self._raio = raio

        # getters e seters para acessar e modificar coordenadas

        def get_raio():
            return self._raio
        def set_raio(self, raio):
            if raio < 0:
                raise ValueError(" O raio deve ser maior que zero")
            self._raio = raio
        #implementação
        def area(self):
            area = 3.14 * (self.raio ** 2)
            return area
        def circunferencia(self):
            circunferencia = 2 * (3.14 * self.raio)
            return circunferencia
        def diametro(self):
            diametro = self.raio * 2
            return diametro
        def nova_posicao(self, novo_x, novo_y):
            self.x = novo_x
            self.y = novo_y
        def __str__(self):
            return f"Circulo(Posicao: ({self.x}, {self.y}, Raio: {self.raio}"

       #objeto dalasse
        circulo = Circulo(10, 10, 7)
        print(circulo)
        print("Área: ", circulo.area())
        print("Diâmetro: ", circulo.diametro())
        print("Circunferência ", circulo.circunferencia())

        #mudando posição:
        circulo.nova_posicao(20, 20)
        print("Nova posição: ", circulo)


