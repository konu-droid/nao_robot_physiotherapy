from naoqi import ALProxy
import time

# Choregraphe bezier export in Python.
def squat(tts, recog, memory, motion):

    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[-0.153442, [3, -0.0133333, 0], [3, 0.386667, 0]], [-0.153442, [3, -0.386667, 0], [3, 0.8, 0]], [-0.150374, [3, -0.8, 0], [3, 0.533333, 0]], [-0.150374, [3, -0.533333, 0], [3, 0.413333, 0]], [-0.150374, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[-4.19617e-05, [3, -0.0133333, 0], [3, 0.386667, 0]], [-4.19617e-05, [3, -0.386667, 0], [3, 0.8, 0]], [-4.19617e-05, [3, -0.8, 0], [3, 0.533333, 0]], [-4.19617e-05, [3, -0.533333, 0], [3, 0.413333, 0]], [-4.19617e-05, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[0.091998, [3, -0.0133333, 0], [3, 0.386667, 0]], [0.0873961, [3, -0.386667, 0], [3, 0.8, 0]], [0.108872, [3, -0.8, 0], [3, 0.533333, 0]], [0.0843279, [3, -0.533333, 0], [3, 0.413333, 0]], [0.0981341, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[-0.110406, [3, -0.0133333, 0], [3, 0.386667, 0]], [-0.110406, [3, -0.386667, 0], [3, 0.8, 0]], [-0.0689882, [3, -0.8, 0], [3, 0.533333, 0]], [-0.122678, [3, -0.533333, 0], [3, 0.413333, 0]], [-0.11194, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[-0.394197, [3, -0.0133333, 0], [3, 0.386667, 0]], [-0.351244, [3, -0.386667, -0.00593118], [3, 0.8, 0.0122714]], [-0.338973, [3, -0.8, 0], [3, 0.533333, 0]], [-0.338973, [3, -0.533333, 0], [3, 0.413333, 0]], [-0.378855, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[-1.17509, [3, -0.0133333, 0], [3, 0.386667, 0]], [-1.15361, [3, -0.386667, 0], [3, 0.8, 0]], [-1.17815, [3, -0.8, 0], [3, 0.533333, 0]], [-1.17815, [3, -0.533333, 0], [3, 0.413333, 0]], [-1.17815, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[0.2936, [3, -0.0133333, 0], [3, 0.386667, 0]], [0.2936, [3, -0.386667, 0], [3, 0.8, 0]], [0.2864, [3, -0.8, 0], [3, 0.533333, 0]], [0.2864, [3, -0.533333, 0], [3, 0.413333, 0]], [0.2864, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[0.124296, [3, -0.0133333, 0], [3, 0.386667, 0]], [0.128898, [3, -0.386667, 0], [3, 0.8, 0]], [-1.36522, [3, -0.8, 0], [3, 0.533333, 0]], [0.128898, [3, -0.533333, -0.00197931], [3, 0.413333, 0.00153396]], [0.130432, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[0.127364, [3, -0.0133333, 0], [3, 0.386667, 0]], [0.127364, [3, -0.386667, 0], [3, 0.8, 0]], [0.01845, [3, -0.8, 0], [3, 0.533333, 0]], [0.1335, [3, -0.533333, 0], [3, 0.413333, 0]], [0.131966, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[-0.167164, [3, -0.0133333, 0], [3, 0.386667, 0]], [-0.167164, [3, -0.386667, 0], [3, 0.8, 0]], [-0.360449, [3, -0.8, 0], [3, 0.533333, 0]], [-0.162562, [3, -0.533333, 0], [3, 0.413333, 0]], [-0.164096, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[-0.0844118, [3, -0.0133333, 0], [3, 0.386667, 0]], [-0.0890141, [3, -0.386667, 0], [3, 0.8, 0]], [1.24557, [3, -0.8, 0], [3, 0.533333, 0]], [-0.092082, [3, -0.533333, 0], [3, 0.413333, 0]], [-0.0798099, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[1.44499, [3, -0.0133333, 0], [3, 0.386667, 0]], [0.0966001, [3, -0.386667, 0], [3, 0.8, 0]], [0.182504, [3, -0.8, 0], [3, 0.533333, 0]], [0.182504, [3, -0.533333, 0], [3, 0.413333, 0]], [1.45266, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[0.177901, [3, -0.0133333, 0], [3, 0.386667, 0]], [-0.00310993, [3, -0.386667, 0], [3, 0.8, 0]], [0.0106959, [3, -0.8, 0], [3, 0.533333, 0]], [0.0106959, [3, -0.533333, 0], [3, 0.413333, 0]], [0.159494, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[0.131882, [3, -0.0133333, 0], [3, 0.386667, 0]], [0.078192, [3, -0.386667, 0.00074142], [3, 0.8, -0.00153397]], [0.076658, [3, -0.8, 0], [3, 0.533333, 0]], [0.076658, [3, -0.533333, 0], [3, 0.413333, 0]], [0.107338, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[0.0828778, [3, -0.0133333, 0], [3, 0.386667, 0]], [0.0828778, [3, -0.386667, 0], [3, 0.8, 0]], [-0.0137641, [3, -0.8, 0], [3, 0.533333, 0]], [0.075208, [3, -0.533333, -0.015835], [3, 0.413333, 0.0122721]], [0.0874801, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[0.113558, [3, -0.0133333, 0], [3, 0.386667, 0]], [0.113558, [3, -0.386667, 0], [3, 0.8, 0]], [0.0614019, [3, -0.8, 0], [3, 0.533333, 0]], [0.112024, [3, -0.533333, 0], [3, 0.413333, 0]], [0.104354, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[0.276162, [3, -0.0133333, 0], [3, 0.386667, 0]], [0.271559, [3, -0.386667, 0.00183274], [3, 0.8, -0.00379187]], [0.259288, [3, -0.8, 0], [3, 0.533333, 0]], [0.259288, [3, -0.533333, 0], [3, 0.413333, 0]], [0.260822, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[1.21335, [3, -0.0133333, 0], [3, 0.386667, 0]], [1.3146, [3, -0.386667, 0], [3, 0.8, 0]], [1.29159, [3, -0.8, 0], [3, 0.533333, 0]], [1.29159, [3, -0.533333, 0], [3, 0.413333, 0]], [1.22409, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[0.2956, [3, -0.0133333, 0], [3, 0.386667, 0]], [0.2956, [3, -0.386667, 0], [3, 0.8, 0]], [0.2948, [3, -0.8, 0], [3, 0.533333, 0]], [0.2948, [3, -0.533333, 0], [3, 0.413333, 0]], [0.2948, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[0.124212, [3, -0.0133333, 0], [3, 0.386667, 0]], [0.124212, [3, -0.386667, 0], [3, 0.8, 0]], [-1.39291, [3, -0.8, 0], [3, 0.533333, 0]], [0.130348, [3, -0.533333, 0], [3, 0.413333, 0]], [0.125746, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[-0.130348, [3, -0.0133333, 0], [3, 0.386667, 0]], [-0.130348, [3, -0.386667, 0], [3, 0.8, 0]], [-0.0643861, [3, -0.8, 0], [3, 0.533333, 0]], [-0.136484, [3, -0.533333, 0.00395863], [3, 0.413333, -0.00306794]], [-0.139552, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[-0.167164, [3, -0.0133333, 0], [3, 0.386667, 0]], [-0.167164, [3, -0.386667, 0], [3, 0.8, 0]], [-0.360449, [3, -0.8, 0], [3, 0.533333, 0]], [-0.162562, [3, -0.533333, 0], [3, 0.413333, 0]], [-0.164096, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[-0.0981341, [3, -0.0133333, 0], [3, 0.386667, 0]], [-0.0981341, [3, -0.386667, 0], [3, 0.8, 0]], [1.34689, [3, -0.8, 0], [3, 0.533333, 0]], [-0.10427, [3, -0.533333, 0], [3, 0.413333, 0]], [-0.0873961, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[1.42666, [3, -0.0133333, 0], [3, 0.386667, 0]], [0.11816, [3, -0.386667, 0], [3, 0.8, 0]], [0.219404, [3, -0.8, 0], [3, 0.533333, 0]], [0.219404, [3, -0.533333, 0], [3, 0.413333, 0]], [1.41899, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[-0.046062, [3, -0.0133333, 0], [3, 0.386667, 0]], [0.033706, [3, -0.386667, 0], [3, 0.8, 0]], [0.0168321, [3, -0.8, 0], [3, 0.533333, 0]], [0.0168321, [3, -0.533333, 0], [3, 0.413333, 0]], [-0.030722, [3, -0.413333, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0, 1.16, 3.56, 5.16, 6.4])
    keys.append([[0.05825, [3, -0.0133333, 0], [3, 0.386667, 0]], [-0.0261199, [3, -0.386667, 0], [3, 0.8, 0]], [0.00149202, [3, -0.8, 0], [3, 0.533333, 0]], [0.00149202, [3, -0.533333, 0], [3, 0.413333, 0]], [0.0475121, [3, -0.413333, 0], [3, 0, 0]]])


    tts.say("Now we will do the sqaut exercise. Get ready.")

    time.sleep(1.0)
    tts.say("Feet shoulder-width, chest up.")

    time.sleep(0.5)
    tts.say("Hips back, knees over toes, weight in heels to lower.")

    time.sleep(0.5)
    tts.say("Squat to depth with neutral spine, core tight.")

    time.sleep(0.5)
    tts.say("Push through heels to stand, squeeze glutes.")

    time.sleep(1.5)
    tts.say("Now, Let me show you how its done")

    # motion.angleInterpolation(names, keys, times, True)
    motion.angleInterpolationBezier(names, times, keys)

    time.sleep(0.5)
    tts.say("All done!")

    return