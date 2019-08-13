import time

class Robot:

    def __init__(self,motorIzquierda1, motorIzquierda2, motorDerecha1, motorDerecha2, sensorUltraSonido):
        self.motoresIzquierda = [motorIzquierda1, motorIzquierda2]
        self.motoresDerecha = [motorDerecha1, motorDerecha2]
        self.sensorUltraSonido = sensorUltraSonido

    def avanzar(self):
        print("ADELANTE")
        for motorIzquierda in self.motoresIzquierda:
            motorIzquierda.avanzar()

        for motorDerecha in self.motoresDerecha:
            motorDerecha.avanzar()


    def retroceder(self):
        print("ATRAS")
        for motorIzquierda in self.motoresIzquierda:
            motorIzquierda.retroceder()

        for motorDerecha in self.motoresDerecha:
            motorDerecha.retroceder()

    def girarDerecha(self):
        print("GIRO DERECHA")
        for motorIzquierda in self.motoresIzquierda:
            motorIzquierda.avanzar()

        for motorDerecha in self.motoresDerecha:
            motorDerecha.retroceder()


    def girarIzquierda(self):
        print("GIRO IZQUIERDA")
        for motorIzquierda in self.motoresIzquierda:
            motorIzquierda.retroceder()

        for motorDerecha in self.motoresDerecha:
            motorDerecha.avanzar()

    def detenerMovimiento(self):
        print("DETENER MOVIMIENTO")
        for motorIzquierda in self.motoresIzquierda:
            motorIzquierda.detener()

        for motorDerecha in self.motoresDerecha:
            motorDerecha.detener()

    def buscarCamino(self):
        print("BUSCANDO CAMINO")

        self.girarDerecha()
        time.sleep(0.5)
        distancia_derecha = self.sensorUltraSonido.distancia
        self.girarIzquierda()
        time.sleep(1)
        distancia_izquierda = self.sensorUltraSonido.distancia

        if(distancia_izquierda < distancia_derecha):
            self.avanzar()
        else:
            self.girarDerecha()
            time.sleep(1)
            self.avanzar()

    def apagar(self):
        self.detenerMovimiento()
