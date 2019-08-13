from agentes.agenteslib.Agent import Agent
from time import sleep, time
import RPi.GPIO as GPIO
import numpy as np
import cv2

class AgentSensorUltraSonido(Agent):


    servo_motor = 21
    p = None
    
    def __init__(self, identificador, contenedor, **kwargs):
        # el diccionario debe contener un 'TIPO' especificando si es 'GPIO' o 'NORMAL, establece si es o no pin
        self.identificador = identificador
        self.contenedor = contenedor
        self.atributos = {'TIPO': 'NINGUNO'} if len(kwargs) == 0 else kwargs
        
        
        GPIO.setup(self.servo_motor, GPIO.OUT)
        
        #self.p = GPIO.PWM(self.servo_motor,50)
        self.p = GPIO.PWM(self.servo_motor,50)
        self.p.start(7.5)
        
        
        
        
        
        self.face_cascade = cv2.CascadeClassifier('cascade2.xml') #se ocupa un modelo ya entrenado y se crea un archivo xml
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3,300)
        
        
        
        
        
        
        super().iniciar_agente(self.action)
        
        
        
        
        
        
        self.hay_obstaculo = False
        self.distancia = 0
        self.distancia_minima = 100
        self.velocidad_sonido_cm_s = 0.0000292

    def __del__(self):
        print("BORRADO")
        
    def delete(self):
        self.cap.release() #libero la camara  
        cv2.destroyAllWindows()

    def medirDistancia(self):
        #GPIO.output(self.atributos['GPIO_TRIG'][0], False)
        #sleep(0.000001)
        GPIO.output(self.atributos['GPIO_TRIG'][0], True)
        sleep(0.0001)
        GPIO.output(self.atributos['GPIO_TRIG'][0], False)

        inicio = time()
        fin = -999
        
        while GPIO.input(self.atributos['GPIO_ECHO'][0]) == 0:
            inicio = time()
            
        
        while GPIO.input(self.atributos['GPIO_ECHO'][0]) == 1:
            fin = time()
        
        duracion = fin-inicio

        # cm:
        return (duracion / self.velocidad_sonido_cm_s)/2  # se divide para dos ya que es el tiempo de ida y vuelta

        """if self.distancia < self.distancia_minima:
            self.enviar_mensaje(self.contenedor.buscar_agente("BROKER"), "Distancia muy corta: %f cm" % self.distancia)
            self.hay_obstaculo = True
            
        else:
            self.enviar_mensaje(self.contenedor.buscar_agente("BROKER"), "Distancia: %f cm" % self.distancia)
            self.hay_obstaculo = False"""
    
    def hardCascade(self,direccion):
        
        for _ in range(30):
        
            self.ret, self.frame = self.cap.read()
            self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY) #convierto a escala de grises, esto trabaja en 2 dimensiones

            self.faces = self.face_cascade.detectMultiScale(self.gray,1.3,5) #densidad y umbral
            if len(self.faces) != 0:
                print("FUEGO FUEGO FUEGO FUEGO FUEGO a la " + direccion)
                return 1
        
        return 0
        
        
        """for (x,y,w,h) in faces: #devuelve posiciones de los rostros
            cv2.rectangle(self.frame,(x,y),(x + w , y + h), (255,0,0), 2)"""
        
    def action(self):
        
        
        
        while Agent.inicio == False:
            sleep(0.5)
        
        
        
        distancias  = []
        camara_fuegos = []
        
        self.p.ChangeDutyCycle(7.5)
        #print("Frente")
        sleep(1)
        distancias.append(self.medirDistancia())
        camara_fuegos.append(self.hardCascade("Frente"))
        
        
        
        sleep(1)
        self.p.ChangeDutyCycle(12.5)
        #print("Izquierda")
        sleep(1)
        distancias.append(self.medirDistancia())
        camara_fuegos.append(self.hardCascade("Izquierda"))
        
        
        sleep(1)
        self.p.ChangeDutyCycle(2.5)
        #print("Derecha")
        sleep(1)
        print("TOMADO")
        distancias.append(self.medirDistancia())
        camara_fuegos.append(self.hardCascade("Derecha"))
        
        #print("MENSAJE")
        self.enviar_mensaje(self.contenedor.buscar_agente("APF"), camara_fuegos)
        self.enviar_mensaje(self.contenedor.buscar_agente("MOVIMIENTO"), distancias)        
        
        Agent.inicio = False

