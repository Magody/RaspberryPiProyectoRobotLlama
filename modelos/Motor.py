import RPi.GPIO as GPIO

class Motor:

    def __init__(self, pin_positivo, pin_negativo):
        self.pins = [pin_positivo, pin_negativo]
        self.setup()

    def setup(self):
        GPIO.setup(self.pins,GPIO.OUT)

    def avanzar(self):
        GPIO.output(self.pins[0], True)
        GPIO.output(self.pins[1], False)

    def retroceder(self):
        GPIO.output(self.pins[0], False)
        GPIO.output(self.pins[1], True)

    def detener(self):
        GPIO.output(self.pins[0], False)
        GPIO.output(self.pins[1], False)


