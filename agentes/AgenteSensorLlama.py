from agentes.agenteslib.Agent import Agent
import RPi.GPIO as GPIO


class AgentSensorLlama(Agent):

    def __init__(self, identificador, contenedor, **kwargs):
        self.identificador = identificador
        self.contenedor = contenedor
        self.atributos = {'TIPO': 'NINGUNO'} if len(kwargs) == 0 else kwargs
        
        super().iniciar_agente(self.action)
        

    def __del__(self):
        print(self.identificador, " HA MUERTO")

    def action(self):

        if GPIO.input(self.atributos['GPIO_DO'][0]) == 1:
            self.enviar_mensaje(self.contenedor.buscar_agente("APF"), 1)
        else:
            self.enviar_mensaje(self.contenedor.buscar_agente("APF"), 0)
