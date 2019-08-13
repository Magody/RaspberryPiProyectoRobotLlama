from agentes.agenteslib.Agent import Agent
import RPi.GPIO as GPIO



class AgentAPF(Agent):

    mensaje_recibido_temperatura = False
    
    mensaje_recibido_llama = False
    mensaje_recibido_explorador = False
    
    
    temperatura = None
    llama = None
    camara = None
    
    def __init__(self, identificador, contenedor, **kwargs):
        self.identificador = identificador
        self.contenedor = contenedor
        self.atributos = {'TIPO': 'NINGUNO'} if len(kwargs) == 0 else kwargs
        
        super().iniciar_agente(self.action)
        

    def __del__(self):
        print(self.identificador, " HA MUERTO")

    def action(self):
        mensajes = self.esperar_mensaje()
        
        for mensaje in mensajes:
        
            if(mensaje.id == "DHT11-APF"):
                #print("Soy " + self.identificador, mensaje.contenido, "recibi de DHT11")
                self.mensaje_recibido_temperatura = True
                self.temperatura = mensaje.contenido
            elif(mensaje.id == "EXPLORADOR-APF"):
                #print("Soy " + self.identificador, mensaje.contenido, "recibi de EXPLORADOR")
                self.mensaje_recibido_explorador = True
                self.camara = mensaje.contenido
                
            elif(mensaje.id == "LLAMA-APF"):
                #print("Soy " + self.identificador, mensaje.contenido, "recibi de Llama")
                self.mensaje_recibido_llama = True
                self.llama = mensaje.contenido
            
            
            
        if(self.mensaje_recibido_temperatura and self.mensaje_recibido_explorador and self.mensaje_recibido_llama ): #and self.mensaje_recibido_llama 
            #print(mensajes[0], type(mensajes[0]),mensajes[0].contenido[0])
            pfs = [self.camara[0]+self.llama+self.temperatura,self.camara[1]+self.llama+self.temperatura,self.camara[2]+self.llama+self.temperatura]
            
            self.enviar_mensaje(self.contenedor.buscar_agente("MOVIMIENTO"), pfs)
            
            self.mensaje_recibido_temperatura = False    
            self.mensaje_recibido_llama = False
            self.mensaje_recibido_explorador = False
    
    
        
        
