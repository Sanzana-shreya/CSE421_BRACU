import socket
import threading
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

def handle_clients(connection,address):

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
                print(message)
                connection.send("Message received ".encode(format))
         
    
                        
                    
    connection.close()


while True:
    connection,address=server.accept()
    thread = threading.Thread(target=handle_clients,args=(connection,address))
    thread.start()