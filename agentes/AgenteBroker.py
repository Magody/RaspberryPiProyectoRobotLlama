from agentes.agenteslib.Agent import Agent
from time import sleep
class AgentBroker(Agent):

    mensaje_recibido_explorador = False
    mensaje_recibido_apf = False
    
    distancias = None
    pfs = None
    
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
            
            
            #print(mensaje.id)
            
            if(mensaje.id == "EXPLORADOR-MOVIMIENTO"):
                print("Soy " + self.identificador, mensaje.contenido, "recibi de EXPLORADOR")
                self.distancias = mensaje.contenido
                self.mensaje_recibido_explorador = True
            elif(mensaje.id == "APF-MOVIMIENTO"):
                print("Soy " + self.identificador, mensaje.contenido, "recibi de APF")
                self.pfs = mensaje.contenido
                self.mensaje_recibido_apf = True
            
                
            
            
            
        #print(self.mensaje_recibido_explorador, self.mensaje_recibido_apf)
        
        if(self.mensaje_recibido_explorador and self.mensaje_recibido_apf):
            print("*"*50)
            print(self.distancias, self.pfs)
            print("*"*50)
            
            
            self.mensaje_recibido_explorador = False
            self.mensaje_recibido_apf = False
            sleep(5)
            Agent.inicio = True
            
            """
            umbral_peligro = 3
            umbral_fuego = 4.5
            distancia_mínima = 30 # En cm


            #0 = frente, 1 = izquierda, 2 = derecha
            indice_mayor_distancia = self.distancias.index(max(self.distancias))
            indice_mayor_pf = self.pfs.index(max(self.pfs))


            if(self.pfs[indice_mayor_pf] >= umbral_fuego):
                #priorizamos la direccion del fuego

                if(indice_mayor_pf == 0):
                    pass
                elif(indice_mayor_pf == 1):
                    self.enviar_mensaje(self.contenedor.buscar_agente("MOTOR_GEAR"), "izquierda detener")
                elif(indice_mayor_pf == 2):
                    self.enviar_mensaje(self.contenedor.buscar_agente("MOTOR_GEAR"), "derecha detener")

                self.enviar_mensaje(self.contenedor.buscar_agente("AGUA"), "encender 3")
                print("MODO TURBO")

            else:
                #no hay fuego, consideramos la direccion de la probabilidad más alta siempre y cuando cumpla
                #con ser mas alto
                self.enviar_mensaje(self.contenedor.buscar_agente("AGUA"), "apagar 0") 

                if(self.pfs[indice_mayor_pf] > umbral_peligro):

                    if(indice_mayor_pf == 0 and self.distancias[0] > distancia_mínima):
                        self.enviar_mensaje(self.contenedor.buscar_agente("MOTOR_GEAR"), "frente avanzar")
                    elif(indice_mayor_pf == 1 and self.distancias[1] > distancia_mínima):
                        self.enviar_mensaje(self.contenedor.buscar_agente("MOTOR_GEAR"), "izquierda avanzar")
                    elif(indice_mayor_pf == 2 and self.distancias[2] > distancia_mínima):
                        self.enviar_mensaje(self.contenedor.buscar_agente("MOTOR_GEAR"), "derecha avanzar")
                    else:
                        #Busca la distancia más grande por defecto
                        if(self.distancias[indice_mayor_distancia] > distancia_mínima):
                            # avanzar lo mueve y lo detiene
                            if(indice_mayor_distancia == 0):
                                self.enviar_mensaje(self.contenedor.buscar_agente("MOTOR_GEAR"), "frente avanzar")
                            elif(indice_mayor_distancia == 1):
                                self.enviar_mensaje(self.contenedor.buscar_agente("MOTOR_GEAR"), "izquierda avanzar")
                            elif(indice_mayor_distancia == 2):
                                self.enviar_mensaje(self.contenedor.buscar_agente("MOTOR_GEAR"), "derecha avanzar")
                        else:
                            #Si la distancia máxima no cumple, las otras tampoco, por lo que se da la vuelta
                            self.enviar_mensaje(self.contenedor.buscar_agente("MOTOR_GEAR"), "reversa avanzar")
                else:
                    #primero la distancia máxima
                    #Si no se puede, entonces da reversa. Si el máximo no cumple los mínimos tampoco
                    if(self.distancias[indice_mayor_distancia] > distancia_mínima):
                        # avanzar lo mueve y lo detiene
                        if(indice_mayor_distancia == 0):
                            self.enviar_mensaje(self.contenedor.buscar_agente("MOTOR_GEAR"), "frente avanzar")
                        elif(indice_mayor_distancia == 1):
                            self.enviar_mensaje(self.contenedor.buscar_agente("MOTOR_GEAR"), "izquierda avanzar")
                        elif(indice_mayor_distancia == 2):
                            self.enviar_mensaje(self.contenedor.buscar_agente("MOTOR_GEAR"), "derecha avanzar")
                    else:
                        #Si la distancia máxima no cumple, las otras tampoco, por lo que se da la vuelta
                        self.enviar_mensaje(self.contenedor.buscar_agente("MOTOR_GEAR"), "reversa avanzar")
            
            """
            
            
            
            
