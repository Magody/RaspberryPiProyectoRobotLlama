from agentes.agenteslib.Agent import Agent
from time import sleep, time
import RPi.GPIO as GPIO


class AgenteMotorGear(Agent):
    ena = 18            
    in1 = 23
    in2 = 24

    enb = 19
    in3 = 6
    in4 = 5
    pwm_a = None
    pwm_b = None
    
    
    tiempo45a = 0.67
    tiempo45b = 0.83
    
    def __init__(self, identificador, contenedor, **kwargs):
        # el diccionario debe contener un 'TIPO' especificando si es 'GPIO' o 'NORMAL, establece si es o no pin
        self.identificador = identificador
        self.contenedor = contenedor
        self.atributos = {'TIPO': 'NINGUNO'} if len(kwargs) == 0 else kwargs
        
        GPIO.setup(self.ena,GPIO.OUT)
        GPIO.setup(self.enb,GPIO.OUT)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.in3, GPIO.OUT)
        GPIO.setup(self.in4, GPIO.OUT)
        self.pwm_a = GPIO.PWM(self.ena,500)
        self.pwm_b = GPIO.PWM(self.enb,500)
        self.pwm_a.start(0)
        self.pwm_b.start(0)
        super().iniciar_agente(self.action)



    def __del__(self):
        print(self.identificador + " HA MUERTO")

    def  Giro_Favor_Reloj_MotorA(self):
        #derecha
        GPIO.output(self.in1,False)
        GPIO.output(self.in2,True)

    def Giro_Contra_Reloj_MotorA(self):
        #derecha
        GPIO.output(self.in1,True)
        GPIO.output(self.in2,False)

   
    def  Giro_Favor_Reloj_MotorB(self):
        #izquierda
        GPIO.output(self.in3,False)
        GPIO.output(self.in4,True)

    def Giro_Contra_Reloj_MotorB(self):
        #izquierda
        GPIO.output(self.in3,True)
        GPIO.output(self.in4,False)
        

    def action(self):
        
        mensajes = self.esperar_mensaje()
        
        
        #Para GEAR
        acciones = mensajes[0].contenido.split()
        
        print(acciones)
        

        if(acciones[0] == "frente"):
            print("NADA")
        elif(acciones[0] == "izquierda"):
            self.Giro_Contra_Reloj_MotorB()
            self.pwm_b.ChangeDutyCycle(int(100))
            self.Giro_Favor_Reloj_MotorA()
            self.pwm_a.ChangeDutyCycle(int(100))
            
            sleep(self.tiempo45b*0.7)
        elif(acciones[0] == "derecha"):
            self.Giro_Contra_Reloj_MotorA()
            self.pwm_a.ChangeDutyCycle(int(100))
            self.Giro_Contra_Reloj_MotorB()
            self.pwm_b.ChangeDutyCycle(int(100))
            sleep(self.tiempo45b*0.8)
        elif(acciones[0] == "reversa"):
            self.Giro_Contra_Reloj_MotorB()
            self.pwm_b.ChangeDutyCycle(int(100))
            self.Giro_Favor_Reloj_MotorA()
            self.pwm_a.ChangeDutyCycle(int(100))
            sleep(self.tiempo45a*1.5)

        if(acciones[1] == "avanzar"):
            self.Giro_Favor_Reloj_MotorA()
            self.pwm_a.ChangeDutyCycle(int(100))
            self.Giro_Favor_Reloj_MotorB()
            self.pwm_b.ChangeDutyCycle(int(100))
            
            sleep(0.5)
            self.pwm_a.stop()
            self.pwm_b.stop()
            
        elif(acciones[1] == "detener"):
            self.pwm_a.stop()
            self.pwm_b.stop()
        
        
