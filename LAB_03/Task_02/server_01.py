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
                print("Terminating connection with client",address)
                connected=False
            else:
                #print(message)
                # #connection.send("Message received ".encode(format))
                vowels="aeiou"
                counter=0
                for i in message:
                    if i in vowels:
                       counter+=1
                if counter==0:
                     connection.send("Not enough vowels".encode(format))
                elif counter <= 3:
                     connection.send("Enough vowels I guess".encode(format))
                else:
                     connection.send("Too many vowels".encode(format))
    
                        
                    
    connection.close()


