from naoqi import ALProxy
import time

def get_knee_status(NAO_IP, NAO_PORT):
    status_words = ["good", "okay", "sore", "painful", "better", "hurts", "bad"]

    try:
        tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
        recog = ALProxy("ALSpeechRecognition", NAO_IP, NAO_PORT)
        memory = ALProxy("ALMemory", NAO_IP, NAO_PORT)

        recog.setLanguage("English")
        recog.setVocabulary(status_words, True)

        tts.say("How is your knee today")
        recog.subscribe("KneeStatus")
        time.sleep(5)

        word = memory.getData("WordRecognized")
        recog.unsubscribe("KneeStatus")

        if word and word[1] > 0.4:
            return word[0]
        else:
            tts.say("I didn't quite hear that")
            return None

    except Exception as e:
        print("Error in knee status", e)
        return None
