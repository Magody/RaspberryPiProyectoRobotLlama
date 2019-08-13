from abc import ABC, abstractmethod
from time import sleep
import RPi.GPIO as GPIO
import threading
from agentes.agenteslib.Mensaje import Mensaje


class Agent(ABC):

    identificador = None
    contenedor = None
    atributos = None
    retardo_bucle = 1
    
    inicio =True
    
    
    @abstractmethod
    def __del__(self):
        pass

    def iniciar_agente(self, action):
        super().__init__()
        self.mensajes = []
        self.esta_vivo = True
        if self.atributos['TIPO'] == 'GPIO':
            self.setup_GPIO()

        threading.Thread(target=lambda: self.comportamiento(action)).start()
        self.contenedor.agregar_agentes(self)

    def setup_GPIO(self):
        for atributo in self.atributos:

            if atributo == 'TIPO':
                continue

            pin = self.atributos[atributo][0]
            modo = self.atributos[atributo][1]

            GPIO.setup(pin, modo)

    def enviar_mensaje(self, agente_destino, msg):
        # el id se pone automáticamente
        mensaje = Mensaje(msg)
        mensaje.id = str(self.identificador) + "-" + str(agente_destino.identificador)
        agente_destino.recibir_mensaje(mensaje)

    def recibir_mensaje(self, mensaje):
        self.mensajes.append(mensaje)

    def esperar_mensaje(self):
        
        while self.mensajes == []:
            sleep(Agent.retardo_bucle)
        msg = self.mensajes
        self.mensajes = []
        return msg

    def destruir(self):
        self.esta_vivo = False
        del self

    def comportamiento(self, action):

        while self.esta_vivo:
            action()
            
            sleep(Agent.retardo_bucle)
        del self  # se elimina a si mismo y llama a take down


"""
from agentes.agenteslib.Agent import Agent


class TemplateAgente(Agent):

    def __init__(self, identificador, contenedor, **kwargs):
        # siempre debe llamar a setup con la función del comportamiento
        self.identificador = identificador
        self.contenedor = contenedor
        self.atributos = {'TIPO': 'NINGUNO'} if len(kwargs) == 0 else kwargs
        
        super().iniciar_agente(self.action)
        
    def __del__(self):
        print(self.identificador, " HA MUERTO")  

    def action(self):
        print("Action")


"""
