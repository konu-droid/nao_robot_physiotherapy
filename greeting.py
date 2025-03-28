import naoqi
import time
from naoqi import ALProxy
from patient_name import recognize_name
from knee_response import get_knee_status
from start_session import wait_for_head_tap, choose_exercise

NAO_IP = "172.18.16.27" 
NAO_PORT = 9559

tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)

tts.say("Hello, my name is Nao, your interactive physiotherapy assistant, here to help with post surgery A C L rehabilitation")
patient_name = recognize_name(NAO_IP, NAO_PORT) #function to ask for patient name 
tts.say("Hi, {}. Nice to meet you".format(patient_name or ""))
time.sleep(5)

knee_status = get_knee_status(NAO_IP, NAO_PORT) #function to ask for knee status
if knee_status:
    tts.say("Thank you for letting me know. You said your knee feels " + knee_status + ".")
else:
    tts.say("Thank you for letting me know")
 
wait_for_head_tap(NAO_IP, NAO_PORT) #function to ask if ready for exercise
time.sleep(5)

exercise_number = choose_exercise(NAO_IP, NAO_PORT) #function to ask for exercise number
if exercise_number:
    exercises = ["Squats", "Leg raises", "Lunges", "Heel slides"]
    selected_exercise = exercises[exercise_number - 1]
    tts.say("You selected " + selected_exercise + "Let's get started")
else:
    tts.say("Let's start with the first exercise")