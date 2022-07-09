import RPi.GPIO as GPIO
import time
import socket
from dotenv import load_dotenv
import os

load_dotenv()

# Get IP and PORT from env.
PORT = int(os.getenv('PORT'))
HOST = os.getenv('HOST')

# Create a socket object
s = socket.socket()

# connect to the server on local computer
s.connect((HOST, PORT))

#set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

#set pin 11 as output, set servo1 as pin 11 as PWM
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50)

#start PWM running, but with value of 0 (off)
servo1.start(0)

#print("goodbye")
# servo1.stop()
#GPIO.cleanup()

def main():
    # receive data from the server and decoding to get the string.
    try:
        duty = (int(s.recv(1024).decode()))
        print("Moving!")
        servo1.ChangeDutyCycle(duty)
    except ValueError:
        pass

if __name__=='__main__':
    while True:
        main()