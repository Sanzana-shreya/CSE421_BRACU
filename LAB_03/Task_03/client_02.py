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

message_to_send(f"Client's ip address: {host_address} and name of client's device {hostname}")
message_to_send(disconnected_message)