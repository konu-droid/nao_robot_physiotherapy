import socket
import json

NAO_IP = "172.18.16.34"  # Replace with NAO’s IP
PORT = 5000

def send_command(command):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((NAO_IP, PORT))

        client_socket.send(json.dumps(command).encode('utf-8'))
        client_socket.close()

    except Exception as e:
        print("Error:", str(e))

while True:
    print("\nChoose a command:")
    print("1. Speak")
    print("2. Walk")
    print("3. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        text = input("Enter text for NAO to say: ")
        send_command({"action": "speak", "text": text})

    elif choice == "2":
        distance = input("Enter distance (meters, e.g., 0.2): ")
        send_command({"action": "walk", "distance": distance})

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")
