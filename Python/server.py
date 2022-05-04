import socket

HOST = "0.0.0.0"
PORT = 6704 #Port Number

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            print(data.decode('utf-8'))
            if data.decode('utf-8').upper() == "DISCONNECT":
               #print("Session Disconnected.")
               conn.close()
               break
