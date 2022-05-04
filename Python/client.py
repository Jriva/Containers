import socket

HOST = "192.168.1.189"  #Loopback IP Address
PORT = 6704         #Port Number

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = " "
    while message.upper() !="DISCONNECT":
        print("Enter Message: ")
        message = input()
        s.sendall(bytes(message,'utf-8'))
    s.close()