from gpiozero import Servo
from time import sleep

from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

servo = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

angle = 0

while True:
    angle = float(input("Enter servo motor angle between -1 and 1: (Enter -5 to break): "))

    if angle == -5:
        print("Setting angle to 180 degrees and quitting")
        servo.value = 0.95
        sleep(1)
        break

    if angle < -1 or angle > 1:
        print("invalid angle entry.")
    else:
        servo.value = angle
        sleep(1)





# servo.value = None;






#Extra code
# # Import libraries
# import RPi.GPIO as GPIO
# import time
# 
# # Set GPIO numbering mode
# GPIO.setmode(GPIO.BOARD)
# 
# # Set pin 11 as an output, and set servo1 as pin 11 as PWM
# GPIO.setup(11,GPIO.OUT)
# servo1 = GPIO.PWM(11,50) # Note 11 is pin, 50 = 50Hz pulse
# 
# #start PWM running, but with value of 0 (pulse off)
# servo1.start(0)
# print ("Waiting for 0.5 seconds")
# time.sleep(0.5)
# 
# # Define variable duty
# duty = 12
# servo1.ChangeDutyCycle(duty)
# # Loop for duty values from 2 to 12 (0 to 180 degrees)
# # while duty <= 12:
# #     servo1.ChangeDutyCycle(duty)
# #     time.sleep(0.3)
# #     servo1.ChangeDutyCycle(0)
# #     time.sleep(0.7)
# #     duty = duty + 1
# 
# #Clean things up at the end
# servo1.stop()
# GPIO.cleanup()
# print ("Goodbye")