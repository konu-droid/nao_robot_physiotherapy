import naoqi
from naoqi import ALProxy

# print("nao lib imported")

tts = ALProxy("ALTextToSpeech", "<IP of your robot>", 9559)
tts.say("Hello, world!")