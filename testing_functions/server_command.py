import socket
import json
import sys
from naoqi import ALProxy

# NAO Configuration
NAO_IP = "127.0.0.1"  # If running directly on NAO, use "127.0.0.1"
PORT = 5000            # Server port

# Initialize Proxies for Speech and Movement
tts = ALProxy("ALTextToSpeech", NAO_IP, 9559)
motion = ALProxy("ALMotion", NAO_IP, 9559)

# Create Server Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", PORT))
server_socket.listen(5)

print "NAO Command Server Started, Listening on Port", PORT

while True:
    client_socket, client_address = server_socket.accept()
    print "Connection received from", client_address

    data = client_socket.recv(1024)
    if not data:
        continue

    try:
        command = json.loads(data)  # Expecting JSON
        action = command.get("action", "")

        if action == "speak":
            text = command.get("text", "Hello")
            print "NAO Speaking:", text
            tts.say(text)

        elif action == "walk":
            distance = float(command.get("distance", 0.2))  # Default: 0.2 meters
            print "NAO Walking:", distance, "meters"
            motion.moveInit()
            motion.moveTo(distance, 0, 0)  # Walk forward

        else:
            print "Unknown Command:", action

    except Exception as e:
        print "Error:", str(e)

    client_socket.close()
