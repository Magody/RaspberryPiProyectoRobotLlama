
"""
# Normal RASPBERRY
"""
import pygame


pygame.init()


sound = pygame.mixer.Sound("../media/sonidos/WALLE/Wall-E_sad.wav")
sound.play()


pygame.time.wait(3000)
pygame.quit()




"""
# Esto funciona en windows sin el pygame.init() ya que eso requiere uan creación de ventana


import time
from pygame import mixer

mixer.init()

# sound = mixer.Sound("C:/Users/Administrador/Desktop/RaspberryPIconAgentesIA-master/ProyectoRobotDetectaLlama/media/sonidos/WALLE/Wall-E_sad.wav")
# sound = mixer.Sound("../media/sonidos/WALLE/Wall-E_sad.wav")



sound.play()

time.sleep(2)

"""