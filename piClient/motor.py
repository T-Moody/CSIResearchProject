import RPi.GPIO as GPIO

# Motor class
class Motor():

    # Initialize motor with pin number.
    def __init__(self, pin):

        GPIO.setwarnings(False)

        # Set GPIO numbering mode
        GPIO.setmode(GPIO.BOARD)

        # Set pin 11 as output, set servo1 as pin 11 as PWM
        GPIO.setup(pin,GPIO.OUT)
        self.servo1 = GPIO.PWM(pin,50)

        # Start PWM running, but with value of 0 (off)
        self.servo1.start(0)

    # Process angle and move motor.
    def move(self, angle):
        self.servo1.ChangeDutyCycle(angle)
    
    # Stop the motor and clean up GPIO
    def stop(self):
        self.servo1.stop()
        GPIO.cleanup()