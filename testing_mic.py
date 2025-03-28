from naoqi import ALProxy
import time

def nao_listen(ip, port):
    # Initialize proxy to ALSpeechRecognition
    tts = ALProxy("ALTextToSpeech", ip, port)
    asr = ALProxy("ALSpeechRecognition", ip, port)
    memory = ALProxy("ALMemory", ip, port)

    # Set language (e.g., 'English')
    asr.setLanguage("English")

    # Pause ASR engine before setting vocabulary
    asr.pause(True)

    # Define words that NAO should recognize
    vocabulary = ["hello", "yes", "no", "stop", "start", "robot"]
    asr.setVocabulary(vocabulary, False)

    # Resume ASR engine after setting vocabulary
    asr.pause(False)

    # Subscribe to the recognition service
    asr.subscribe("Test_ASR")
    print("Listening... Speak clearly.")

    # time.sleep(10)

    try:
        while True:
            time.sleep(1)
            data = memory.getData("WordRecognized")
            if data and data[0] in vocabulary:
                print("NAO heard: {} with confidence {:.2f}".format(data[0], data[1]))
    except KeyboardInterrupt:
        print("Stopping NAO listening service.")
        asr.unsubscribe("Test_ASR")

if __name__ == "__main__":
    nao_ip = "172.18.16.27"  # Replace with NAO's IP address
    nao_port = 9559           # Default NAOqi port
    nao_listen(nao_ip, nao_port)
