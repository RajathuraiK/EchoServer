# Echoserver
Echo server and client using python socket

# AIM:

To develop a simple webserver to serve html programming pages.

## DESIGN STEPS:

### Step 1:

Design of echo server and client using python socket

### Step 2:

Implementation using Python code

### Step 3:

Testing the server and client 

## PROGRAM:

### server.py
```

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
```

### client.py
```

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
```

## OUTPUT:


## RESULT:
The program is executed successfully
