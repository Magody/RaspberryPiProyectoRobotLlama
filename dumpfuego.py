from time import sleep, time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

GPIO.setup(22,GPIO.IN)


for _ in range(10):
    if GPIO.input(22) == 1:
        print(1)
    else:
        print(0)
            
    sleep(1)


GPIO.cleanup()
exit(0)