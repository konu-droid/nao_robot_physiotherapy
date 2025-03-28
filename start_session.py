from naoqi import ALProxy
import time

def wait_for_head_tap(NAO_IP, NAO_PORT):
    tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
    memory = ALProxy("ALMemory", NAO_IP, NAO_PORT)
    
    tts.say("If you are ready to start your A C L exercises, tap my head")

    while True:
        # adding all three touch sensors from the head so that it can sense tap from everywhere
        head_touch = memory.getData("Device/SubDeviceList/Head/Touch/Front/Sensor/Value")
        head_touch += memory.getData("Device/SubDeviceList/Head/Touch/Middle/Sensor/Value")
        head_touch += memory.getData("Device/SubDeviceList/Head/Touch/Rear/Sensor/Value")
        
        if head_touch > 0.5:
            print("Head was tapped")
            break
        time.sleep(0.2)

def choose_exercise(NAO_IP, NAO_PORT):
    tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
    recog = ALProxy("ALSpeechRecognition", NAO_IP, NAO_PORT)
    memory = ALProxy("ALMemory", NAO_IP, NAO_PORT)

    tts.say("Great, I have 4 exercises for you")
    tts.say("1. Squats, 2. Leg raises, 3. Lunges, 4. Heel slides")
    tts.say("Which exercise would you like to start with? Please say a number from 1 to 4")

    vocab = ["one", "two", "three", "four"]
    recog.setLanguage("English")
    # Pause ASR engine before setting vocabulary
    recog.pause(True)
    recog.setVocabulary(vocab, False)
    recog.pause(False)

    recog.subscribe("ExerciseChoice")
    time.sleep(5)
    result = memory.getData("WordRecognized")
    recog.unsubscribe("ExerciseChoice")
    print(result)

    if result[1] > 0.4:
        spoken_number = result[0]
        exercise_number = vocab.index(spoken_number) + 1
        print("exercise_number: ", exercise_number)
        return exercise_number
    else:
        tts.say("I didn't catch that, let's try again")
        return None
