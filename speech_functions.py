from naoqi import ALProxy
import time

def recognize_name(tts: ALProxy, recog: ALProxy, memory: ALProxy):
    name_list = ["Claire", "Mohan", "Usamah", "Conah", "Jack"]

    try:
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
    
def get_knee_status(tts: ALProxy, recog: ALProxy, memory: ALProxy):
    status_words = ["good", "okay", "sore", "painful", "better", "hurts", "bad"]

    try:
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
    
def choose_exercise(tts: ALProxy, recog: ALProxy, memory: ALProxy):
    
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

# # testing code delete after use
# if __name__ == "__main__":
#     nao_ip = "172.18.16.27"  # Replace with NAO's IP address
#     nao_port = 9559           # Default NAOqi port
#     recognize_name(nao_ip, nao_port)