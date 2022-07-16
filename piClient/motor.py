import RPi.GPIO as GPIO

# Motor class
class Motor():

    def __init__(self, pin):

        GPIO.setwarnings(False)

        # set GPIO numbering mode
        GPIO.setmode(GPIO.BOARD)

        # set pin 11 as output, set servo1 as pin 11 as PWM
        GPIO.setup(pin,GPIO.OUT)
        self.servo1 = GPIO.PWM(pin,50)

        # start PWM running, but with value of 0 (off)
        self.servo1.start(0)

    def move(self, angle):
        self.servo1.ChangeDutyCycle(angle)
    
    def stop(self):
        self.servo1.stop()
        GPIO.cleanup()