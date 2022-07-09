# Main Connects to the client and sends inputs to client.
import socket
import time
from threading import Thread
from dotenv import load_dotenv
import os

load_dotenv()

# Get IP and PORT from env.
PORT= int(os.getenv('PORT'))
HOST = os.getenv('HOST')

# Start server
socketserver = socket.socket()
host = HOST
port = PORT
socketserver.bind((host, port))
socketserver.listen(5)

# Wait for client connection.
clientSocket, address = socketserver.accept()

# While the connection is good, send inputs to client.
def main():
    
    # Convert input to binary and send to client.
    clientSocket.send(bin(int().encode(4)))

    # Delay to not overwhelm the client.
    time.sleep(1)

if __name__ == '__main__':
    while True:
        main()