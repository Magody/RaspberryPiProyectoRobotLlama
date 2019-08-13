from agentes.agenteslib.Contenedor import Contenedor
from agentes.AgenteUltraSonido import AgentSensorUltraSonido
from agentes.AgenteDHT11 import AgentDHT11
from agentes.AgenteBroker import AgentBroker
from agentes.AgenteSensorLlama import AgentSensorLlama
from agentes.AgenteMotorGear import AgenteMotorGear
from agentes.AgenteAPF import AgentAPF
from agentes.AgenteBombaAgua import AgentBombaAgua

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


# inicio de agentes
contenedor = Contenedor()
agenteAgua = AgentBombaAgua("AGUA", contenedor)
agenteBroker = AgentBroker("MOVIMIENTO", contenedor)  #recibira los mensajes
agenteUltraSonido = AgentSensorUltraSonido("EXPLORADOR", contenedor, **{'TIPO': 'GPIO', 'GPIO_TRIG': [4, GPIO.OUT], 'GPIO_ECHO': [17, GPIO.IN]})
agenteAPF = AgentAPF("APF", contenedor)
agenteMotorGear = AgenteMotorGear("MOTOR_GEAR", contenedor)

agenteDHT11 = AgentDHT11("DHT11", contenedor, 27)
agenteLlama = AgentSensorLlama("LLAMA", contenedor, **{'TIPO': 'GPIO', 'GPIO_DO': [22, GPIO.IN]})


sleep(20)

GPIO.cleanup()
exit(0)

