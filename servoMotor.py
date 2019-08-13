import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)
p = GPIO.PWM(21,50)
p.start(7.5)

try:
    while True:
        p.ChangeDutyCycle(7.5)
        print("Frente")
        time.sleep(1)
        p.ChangeDutyCycle(12.5)
        print("Izquierda")
        time.sleep(1)
        p.ChangeDutyCycle(2.5)
        print("Derecha")
        time.sleep(1)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup