
import socket

# Create a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server to an IP address and port
server.bind(('127.0.0.1', 5000))

# Start listening for connections
server.listen(1)

print("Echo Server is running...")
print("Waiting for client connection...")

# Accept a client connection
conn, addr = server.accept()

print("Connected to:", addr)

while True:
    # Receive data from client
    data = conn.recv(1024)

    if not data:
        break

    # Display received message
    print("Client:", data.decode())

    # Send the same message back
    conn.sendall(data)

conn.close()
server.close()