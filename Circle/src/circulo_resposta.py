class Circulo:
    def __init__(self, cx, cy, r):

        self.centrox = cx
        self.centroy = cy
        self.raio
        def area(self):
           return 3.14 * self.raio ** 2
        def circunferencia(self):
            return 2 * 3.14 * self.raio
        def diametro(self):
            return self.raio * 2
        def mover(self, x, y):
            self.centrox = x
            self.centroy = y


       #objeto dalasse
        c1 = Circulo(0, 0, 1)

        print(c1.area())
        print(c1.diametro())
        print(c1.circunferencia())

        #mudando posição:
        c1.mover(0, 0, 1)
        print(c1.centrox)
        print(c1.centroy)


