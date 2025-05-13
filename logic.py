from naoqi import ALProxy
import time

from exercises.squat import squat
from exercises.side_lunge import side_lunge
from exercises.lunge import lunge
from exercises.heel_slide import heel_slide

def perform_exercise(first_idx, patient_name, tts, recog, memory, motion, posture):

    execises_set = {1, 2, 3, 4}

    exercise_map(first_idx, tts, recog, memory, motion, posture)

    execises_set.remove(first_idx)

    for exercise_idx in execises_set: 
        exercise_map(exercise_idx, tts, recog, memory, motion, posture)

    return

def exercise_map(exercise_idx, tts, recog, memory, motion, posture):
    # Feel free to add what ever parameters you wanna add
    if exercise_idx == 1:
        squat(tts, recog, memory, motion)
    if exercise_idx == 2:
        side_lunge(tts, recog, memory, motion)
    if exercise_idx == 3:
        lunge(tts, recog, memory, motion)
    if exercise_idx == 4:
        heel_slide(tts, motion, posture)

    # squat(tts, recog, memory, motion)