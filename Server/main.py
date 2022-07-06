# Main Connects to the client and sends inputs to client.
import socket
import time
from threading import Thread

# Start server
socketserver = socket.socket()
host = ''
port = 8000
socketserver.bind((host, port))
socketserver.listen(5)

# Wait for client connection.
clientSocket, address = socketserver.accept()

# While the connection is good, send inputs to client.
def main():
    
    # Convert input to binary and send to client.
    clientSocket.send(bin(int().encode())
    clientSocket.send(bin(int().encode())

    # Delay to not overwhelm the client.
    time.sleep(.1)

if __name__ == '__main__':
    while True:
        main()