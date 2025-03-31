from naoqi import ALProxy

NAO_IP = "172.18.16.27"  # Replace with your robot's IP
NAO_PORT = 9559

tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
tts.say("Hello! I am NAO, your friendly robot.")

