import socket
data=16
port=5050
format='UTF-8'


hostname=socket.gethostname()
host_address=socket.gethostbyname(hostname)

server_socket_address=(host_address,port)
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
disconnected_message="off"
server.bind(server_socket_address)
server.listen()
print("Server is listening")

while True:
    connection,address=server.accept()
    connected=True

    print(f"Client{address} has connected to the server")
    while connected:
        initial_message=connection.recv(data).decode(format)
        print(f"Length of message is",initial_message)



        if initial_message:
            message_length=int(initial_message)
            message=connection.recv(message_length).decode(format)
            if message==disconnected_message:
                connection.send("Goodbye!").encode(format)
                print("Termonating connection with client",address)
                connected=False
            else:
                hour = int(message)
                salary = 0
                if hour <= 40:
                    salary += (hour*200)
                else:
                    salary += (8000 + (300*(hour-40)))
                connection.send(f"The salary of the person is {salary}".encode(format))
         
    
                        
                    
    connection.close()


