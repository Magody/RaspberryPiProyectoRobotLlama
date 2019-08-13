from time import sleep
import threading

class Contenedor:

    retardo_bucle = 1

    def __init__(self):
        self.esta_vivo = True
        self.agentes = []
        threading.Thread(target=self.monitorear_agentes).start()


    def agregar_agentes(self, agente):
        self.agentes.append(agente)

    def buscar_agente(self, identificador):

        for agente in self.agentes:
            if agente.identificador == identificador:
                return agente

        return None

    def monitorear_agentes(self):

        while self.esta_vivo:

            if len(self.agentes) > 0:

                for i in range(len(self.agentes)):
                    if not self.agentes[i].esta_vivo:
                        del self.agentes[i]
                        self.agentes.pop(i)
                        if len(self.agentes) == 0:
                            self.esta_vivo = False
                        break

            sleep(Contenedor.retardo_bucle)
