
import socket

# Create a TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect(('127.0.0.1', 5000))

while True:
    # Get message from user
    message = input("Enter message (type exit to quit): ")

    if message.lower() == "exit":
        break

    # Send message to server
    client.sendall(message.encode())

    # Receive echoed message
    response = client.recv(1024)

    print("Server:", response.decode())

client.close()