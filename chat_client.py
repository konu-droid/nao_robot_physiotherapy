


# THis goes on the robot, tested it and it works. works in combination with chat_server.py



from naoqi import ALProxy
import time
import socket
import os

# Get the local machine's IP address
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))  # Connects to an external server to determine local IP
    ip = s.getsockname()[0]
    s.close()
    return ip

# Robot IP and port
robot_IP = get_local_ip()
robot_PORT = 9559  # Default NAO port

# Initialize the proxies
record = ALProxy("ALAudioRecorder", robot_IP, robot_PORT)
tts = ALProxy("ALTextToSpeech", robot_IP, robot_PORT)

# Start speaking on the robot
tts.say("Hello, world!")

record_path = "/home/nao/audio_recordings/mohan_voice.wav"  # Change path if needed

# Start recording audio
record.startMicrophonesRecording(record_path, 'wav', 16000, (0, 0, 1, 0))

# Wait for the recording to finish
time.sleep(5)
record.stopMicrophonesRecording()

# Send file to found server
server_IP = "172.18.16.21"
server_PORT = 5001

if server_IP:
    def send_file(file_path, server_ip, server_port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((server_ip, server_port))

            file_size = os.path.getsize(file_path)

            # Send file name and size first
            file_info = "{}|{}".format(os.path.basename(file_path), file_size)
            sock.send(file_info.encode())

            # Wait for acknowledgment
            sock.recv(1024)

            # Send the file in chunks
            with open(file_path, "rb") as file:
                while True:
                    chunk = file.read(4096)
                    if not chunk:
                        break
                    sock.send(chunk)

            print("File sent successfully!")
            sock.close()
        except Exception as e:
            print("Error sending file:", str(e))

    # Call function to send the file
    send_file(record_path, server_IP, server_PORT)
else:
    print("No server found. File not sent.")
