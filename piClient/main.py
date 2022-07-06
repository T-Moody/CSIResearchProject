import RPi.GPIO as GPIO
import time

#set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

#set pin 11 as output, set servo1 as pin 11 as PWM
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50)

#start PWM running, but with value of 0 (off)
servo1.start(0)

print("Moving!")
servo1.ChangeDutyCycle(2)
time.sleep(5)



print("goodbye")
servo1.stop()
GPIO.cleanup()