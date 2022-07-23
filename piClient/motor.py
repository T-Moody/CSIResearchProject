from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

# Motor class
class Motor():

    # Initialize motor with pin number.
    def __init__(self, pin):

        self.servo = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/10)

    # Process angle and move motor. Takes in number from -100 to 100.
    def move(self, angle):
        self.servo.value = float(angle) / 100

    # Stop the motor and clean up GPIO
    def stop(self):
        self.servo.value = 0.95
        sleep(1)
