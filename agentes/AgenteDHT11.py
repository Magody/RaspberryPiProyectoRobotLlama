from agentes.agenteslib.Agent import Agent
from agentes.agenteslib import DHT11

class AgentDHT11(Agent):

    def __init__(self, identificador, contenedor, GPIO_PIN, **kwargs):
        # siempre debe llamar a setup con la función del comportamiento
        self.identificador = identificador
        self.contenedor = contenedor
        self.atributos = {'TIPO': 'NINGUNO'} if len(kwargs) == 0 else kwargs
        
        self.instance = DHT11.DHT11(pin=GPIO_PIN)
        super().iniciar_agente(self.action)
        
    def __del__(self):
        print(self.identificador, " HA MUERTO")    
        

    def action(self):
        result = self.instance.read()
        if result.is_valid():
            self.enviar_mensaje(self.contenedor.buscar_agente("APF"), (result.temperature / (result.humidity/100))/30)
