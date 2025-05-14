import naoqi
import time
from naoqi import ALProxy
from speech_functions import recognize_name, choose_exercise
from speech_functions import get_knee_status, get_end_feedback
from sensors import wait_for_head_tap
from logic import perform_exercise

NAO_IP = "172.18.16.54" 
NAO_PORT = 9559

if __name__ == "__main__":
    tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
    recog = ALProxy("ALSpeechRecognition", NAO_IP, NAO_PORT)
    memory = ALProxy("ALMemory", NAO_IP, NAO_PORT)
    motion = ALProxy("ALMotion", NAO_IP, NAO_PORT)
    posture = ALProxy("ALRobotPosture", NAO_IP , NAO_PORT)

    tts.say("Hello, my name is Dewey, your interactive physiotherapy assistant, here to help with post surgery A C L rehabilitation")
    patient_name = recognize_name(tts, recog, memory) #function to ask for patient name 
    tts.say("Hi, {}. Nice to meet you".format(patient_name or ""))
    time.sleep(2)

    knee_status = get_knee_status(tts, recog, memory) #function to ask for knee status
    if knee_status:
        tts.say("Thank you for letting me know. You said your knee feels " + knee_status + ".")
    else:
        tts.say("Thank you for letting me know")
    
    wait_for_head_tap(tts, recog, memory) #function to ask if ready for exercise
    time.sleep(1)

    # By default we start with first exercise
    exercise_number = choose_exercise(tts, recog, memory) #function to ask for exercise number
    
    if exercise_number:
        exercises = ["Squats", "Leg raises", "Lunges", "Heel slides"]
        selected_exercise_name = exercises[exercise_number - 1]
        tts.say("You selected " + selected_exercise_name + "Let's get started")
    else:
        tts.say("Let's start with the first exercise")

    # add logic to perform all the actions one after the other
    # perform the exercise selected
    perform_exercise(exercise_number, patient_name, tts, recog, memory, motion, posture)
    # perform_exercise(1, "mohan", tts, recog, memory, motion, posture)

    feedback = get_end_feedback(tts, recog, memory)
    if feedback:
        tts.say("Thank you for letting me know. You said your the session was " + feedback + ". I will update the feedback log!")
        time.sleep(0.5)
        tts.say("Great! That will be the end of the session. Please take care. bye!")
    else:
        tts.say("Great! That will be the end of the session. Please take care. bye!")




    