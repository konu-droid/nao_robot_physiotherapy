from naoqi import ALProxy
import time

from exercises.squat import squat
from exercises.leg_raises import leg_raises
from exercises.lunge import lunge
from exercises.heel_slide import heel_slide

def perform_exercise(exercise_idx: int, patient_name: str, tts: ALProxy, recog: ALProxy, memory: ALProxy):

    # Feel free to add what ever parameters you wanna add
    if exercise_idx == 1:
        squat()
    if exercise_idx == 2:
        leg_raises()
    if exercise_idx == 3:
        lunge()
    if exercise_idx == 4:
        heel_slide()


    return