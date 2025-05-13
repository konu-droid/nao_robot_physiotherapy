from naoqi import ALProxy
import time

def wait_for_head_tap(tts, recog, memory):
    
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


