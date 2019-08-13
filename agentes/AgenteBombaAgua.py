from agentes.agenteslib.Agent import Agent
from time import sleep

import RPi.GPIO as GPIO

class AgentBombaAgua(Agent):

    
    def __init__(self, identificador, contenedor, **kwargs):
        self.identificador = identificador
        self.contenedor = contenedor
        self.atributos = {'TIPO': 'NINGUNO'} if len(kwargs) == 0 else kwargs
        
        GPIO.setup(25,GPIO.OUT)
        




        super().iniciar_agente(self.action)
        

    def __del__(self):
        print(self.identificador, " HA MUERTO")

    def action(self):
        mensajes = self.esperar_mensaje()
        
        acciones = mensajes[0].contenido.split()

        if(acciones[0] == "encender"):
            GPIO.output(25,GPIO.HIGH)


        elif(acciones[0] == "apagar"):
            GPIO.output(25,GPIO.LOW)

        sleep(int(acciones[1]))
            
        
