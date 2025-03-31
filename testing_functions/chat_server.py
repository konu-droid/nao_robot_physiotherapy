
# Tested 


import socket
import os
import time
import threading

server_PORT = 5001
save_directory = "./received_files/"

if not os.path.exists(save_directory):
    os.makedirs(save_directory)

def get_server_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

server_IP = get_server_ip()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_IP, server_PORT))
server_socket.listen(1)

print("Server running at {}:{}".format(server_IP, server_PORT))

# Broadcast server presence
def broadcast_server():
    broadcast_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    broadcast_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    while True:
        print("Broadcasting server presence...")
        broadcast_sock.sendto("SERVER_HERE".encode(), ("255.255.255.255", server_PORT))
        time.sleep(5)

threading.Thread(target=broadcast_server).start()

while True:
    conn, addr = server_socket.accept()
    print("Connected to", addr)

    file_info = conn.recv(1024).decode()
    file_name, file_size = file_info.split("|")
    file_size = int(file_size)

    conn.send("OK".encode())

    file_path = os.path.join(save_directory, file_name)
    with open(file_path, "wb") as file:
        received_bytes = 0
        while received_bytes < file_size:
            chunk = conn.recv(4096)
            if not chunk:
                break
            file.write(chunk)
            received_bytes += len(chunk)

    print("Received:", file_name)
    conn.close()
