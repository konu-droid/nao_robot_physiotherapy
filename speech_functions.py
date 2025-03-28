from naoqi import ALProxy
import time

def recognize_name(NAO_IP, NAO_PORT):
    name_list = ["Claire", "Mohan", "Usamah", "Conah", "Jack"]

    try:
        tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
        recog = ALProxy("ALSpeechRecognition", NAO_IP, NAO_PORT)
        memory = ALProxy("ALMemory", NAO_IP, NAO_PORT)

        recog.setLanguage("English")
        # Pause ASR engine before setting vocabulary
        recog.pause(True)
        recog.setVocabulary(name_list, False)
        recog.pause(False)

        tts.say("What is your name")
        recog.subscribe("NameRecognition")
        time.sleep(5)

        word = memory.getData("WordRecognized")
        recog.unsubscribe("NameRecognition")

        if word[1] > 0.4:
            print(word)
            return word[0]
        else:
            tts.say("Sorry, I didn't catch that")
            return None

    except Exception as e:
        print("Error during name recognition", e)
        return None
    
def get_knee_status(NAO_IP, NAO_PORT):
    status_words = ["good", "okay", "sore", "painful", "better", "hurts", "bad"]

    try:
        tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
        recog = ALProxy("ALSpeechRecognition", NAO_IP, NAO_PORT)
        memory = ALProxy("ALMemory", NAO_IP, NAO_PORT)

        recog.setLanguage("English")
        # Pause ASR engine before setting vocabulary
        recog.pause(True)
        recog.setVocabulary(status_words, True)
        recog.pause(False)

        tts.say("How is your knee today")
        recog.subscribe("KneeStatus")
        time.sleep(5)

        word = memory.getData("WordRecognized")
        recog.unsubscribe("KneeStatus")

        if word[1] > 0.4:
            return word[0]
        else:
            tts.say("I didn't quite hear that")
            return None

    except Exception as e:
        print("Error in knee status", e)
        return None

# # testing code delete after use
# if __name__ == "__main__":
#     nao_ip = "172.18.16.27"  # Replace with NAO's IP address
#     nao_port = 9559           # Default NAOqi port
#     recognize_name(nao_ip, nao_port)