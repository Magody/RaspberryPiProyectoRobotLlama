from time import sleep, time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

GPIO.setup(25,GPIO.OUT)

GPIO.output(25,GPIO.HIGH)

sleep(10)
GPIO.output(25,GPIO.LOW)
GPIO.cleanup()
exit(0)