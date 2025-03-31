from naoqi import ALProxy
import time
import socket
import os

# Robot IP and port
robot_IP = "172.18.16.27"
robot_PORT = 9559

# Receiving computer details
server_IP = "172.18.16.21"  # Change to the actual receiving computer's IP
server_PORT = 5001           # Choose an available port

# Initialize the proxies
record = ALProxy("ALAudioRecorder", robot_IP, robot_PORT)
tts = ALProxy("ALTextToSpeech", robot_IP, robot_PORT)

# Start speaking on the robot
tts.say("Hello, world!")

record_path = "/home/nao/audio_recordings/test.wav"

# Start recording audio
record.startMicrophonesRecording(record_path, 'wav', 16000, (0, 0, 1, 0))

# Wait for the recording to finish
time.sleep(5)
record.stopMicrophonesRecording()

# Function to send file
def send_file(file_path, server_ip, server_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((server_ip, server_port))

        # Get file size
        file_size = os.path.getsize(file_path)

        # Send file name and size first
        file_info = "{}|{}".format(os.path.basename(file_path), file_size)
        sock.send(file_info)

        # Wait for acknowledgment
        sock.recv(1024)

        # Send the file in chunks
        with open(file_path, "rb") as file:
            while True:
                chunk = file.read(4096)
                if not chunk:
                    break
                sock.send(chunk)

        print "File sent successfully!"
        sock.close()
    except Exception as e:
        print "Error sending file:", str(e)

# Call function to send the file
send_file(record_path, server_IP, server_PORT)
