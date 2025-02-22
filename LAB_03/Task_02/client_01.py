import socket
data=16
port=5050
format='UTF-8'


hostname=socket.gethostname()
host_address=socket.gethostbyname(hostname)

server_socket_address = (host_address, port)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_socket_address)
disconnected_message="off"

def message_to_send(message):
    message = message.encode(format)
    message_length=len(message)
    send_length = str(len(message)).encode(format)
    send_length += b" " * (data- len(send_length))

    client.send(send_length)
    client.send(message)

    print(client.recv(2048).decode(format))


connected=True
while connected:
    message=input("Enter your message")
    if message=="Done":
        connected=False
        message_to_send(disconnected_message)
    else:
        message_to_send(message)

#send_message(f"Client's IP Address: {host_ip_addr} and Device Name is {host_name}.")
#send_message(close)