import time
import socket
from dotenv import load_dotenv
import os
from motor import Motor

load_dotenv()

# Get IP and PORT from env.
PORT = int(os.getenv('PORT'))
HOST = os.getenv('HOST')

# Create a socket object
s = socket.socket()

# connect to the server on local computer
s.connect((HOST, PORT))

# Create motor object pass in pin number
motor = Motor(11)

def main():
    # receive data from the server and decoding to get the int value.
    try:
        duty = (int(s.recv(1024).decode(), 0))
        print("Duty: " + str(duty))
        
        # Shutdown if 0 is received from server.
        if duty == 0 :
            motor.stop()
            time.sleep(0.5)
            exit()
        
        # Move motor.
        print("Moving!")
        motor.move(duty)
        
    except ValueError:
        pass

if __name__ == '__main__':
    while True:
        main()
