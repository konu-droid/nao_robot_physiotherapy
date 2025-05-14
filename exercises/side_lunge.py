from naoqi import ALProxy
import time

def side_lunge(tts, recog, memory, motion):

    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0, 3.96, 6])
    keys.append([[-0.150374, [3, -0.0133333, 0], [3, 1.32, 0]], [0.0137641, [3, -1.32, 0], [3, 0.68, 0]], [-0.128898, [3, -0.68, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([0, 3.96, 6])
    keys.append([[-4.19617e-05, [3, -0.0133333, 0], [3, 1.32, 0]], [-0.00157595, [3, -1.32, 0], [3, 0.68, 0]], [-0.00157595, [3, -0.68, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([0, 3.96, 6])
    keys.append([[0.10427, [3, -0.0133333, 0], [3, 1.32, 0]], [-1.19503, [3, -1.32, 0], [3, 0.68, 0]], [0.116542, [3, -0.68, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([0, 3.96, 6])
    keys.append([[-0.116542, [3, -0.0133333, 0], [3, 1.32, 0]], [0.0767419, [3, -1.32, 0], [3, 0.68, 0]], [-0.121144, [3, -0.68, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0, 3.96, 6])
    keys.append([[-0.37272, [3, -0.0133333, 0], [3, 1.32, 0]], [-0.977116, [3, -1.32, 0], [3, 0.68, 0]], [-0.371186, [3, -0.68, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0, 3.96, 6])
    keys.append([[-1.17815, [3, -0.0133333, 0], [3, 1.32, 0]], [-1.34536, [3, -1.32, 0], [3, 0.68, 0]], [-1.2073, [3, -0.68, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0, 3.96, 6])
    keys.append([[0.2864, [3, -0.0133333, 0], [3, 1.32, 0]], [0.2428, [3, -1.32, 0], [3, 0.68, 0]], [0.2732, [3, -0.68, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([0, 3.96, 6])
    keys.append([[0.135034, [3, -0.0133333, 0], [3, 1.32, 0]], [-0.754686, [3, -1.32, 0], [3, 0.68, 0]], [0.1335, [3, -0.68, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([0, 3.96, 6])
    keys.append([[0.130432, [3, -0.0133333, 0], [3, 1.32, 0]], [0.0844118, [3, -1.32, 0], [3, 0.68, 0]], [0.131966, [3, -0.68, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([0, 3.96, 6])
    keys.append([[-0.153358, [3, -0.0133333, 0], [3, 1.32, 0]], [-0.00762796, [3, -1.32, 0], [3, 0.68, 0]], [-0.154892, [3, -0.68, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([0, 3.96, 6])
    keys.append([[-0.0844118, [3, -0.0133333, 0], [3, 1.32, 0]], [2.13222, [3, -1.32, 0], [3, 0.68, 0]], [-0.0890141, [3, -0.68, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0, 3.96, 6])
    keys.append([[1.40357, [3, -0.0133333, 0], [3, 1.32, 0]], [1.40357, [3, -1.32, 0], [3, 0.68, 0]], [1.41431, [3, -0.68, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0, 3.96, 6])
    keys.append([[0.174835, [3, -0.0133333, 0], [3, 1.32, 0]], [0.289883, [3, -1.32, 0], [3, 0.68, 0]], [0.194775, [3, -0.68, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0, 3.96, 6])
    keys.append([[0.107338, [3, -0.0133333, 0], [3, 1.32, 0]], [0.0168321, [3, -1.32, 0], [3, 0.68, 0]], [0.0720561, [3, -0.68, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([0, 3.96, 6])
    keys.append([[0.0859461, [3, -0.0133333, 0], [3, 1.32, 0]], [-0.185572, [3, -1.32, 0], [3, 0.68, 0]], [0.0890141, [3, -0.68, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([0, 3.96, 6])
    keys.append([[0.107422, [3, -0.0133333, 0], [3, 1.32, 0]], [-0.0536479, [3, -1.32, 0], [3, 0.68, 0]], [0.113558, [3, -0.68, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0, 3.96, 6])
    keys.append([[0.262356, [3, -0.0133333, 0], [3, 1.32, 0]], [0.503194, [3, -1.32, 0], [3, 0.68, 0]], [0.26389, [3, -0.68, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0, 3.96, 6])
    keys.append([[1.25477, [3, -0.0133333, 0], [3, 1.32, 0]], [1.34681, [3, -1.32, 0], [3, 0.68, 0]], [1.27931, [3, -0.68, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0, 3.96, 6])
    keys.append([[0.2948, [3, -0.0133333, 0], [3, 1.32, 0]], [0.2364, [3, -1.32, 0], [3, 0.68, 0]], [0.2808, [3, -0.68, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([0, 3.96, 6])
    keys.append([[0.136484, [3, -0.0133333, 0], [3, 1.32, 0]], [0.329768, [3, -1.32, 0], [3, 0.68, 0]], [0.12728, [3, -0.68, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([0, 3.96, 6])
    keys.append([[-0.144154, [3, -0.0133333, 0], [3, 1.32, 0]], [-0.799172, [3, -1.32, 0], [3, 0.68, 0]], [-0.154892, [3, -0.68, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([0, 3.96, 6])
    keys.append([[-0.153358, [3, -0.0133333, 0], [3, 1.32, 0]], [-0.00762796, [3, -1.32, 0], [3, 0.68, 0]], [-0.154892, [3, -0.68, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([0, 3.96, 6])
    keys.append([[-0.0904641, [3, -0.0133333, 0], [3, 1.32, 0]], [-0.093532, [3, -1.32, 0.00236235], [3, 0.68, -0.00121697]], [-0.101202, [3, -0.68, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0, 3.96, 6])
    keys.append([[1.3699, [3, -0.0133333, 0], [3, 1.32, 0]], [1.39445, [3, -1.32, 0], [3, 0.68, 0]], [1.36223, [3, -0.68, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0, 3.96, 6])
    keys.append([[-0.0813439, [3, -0.0133333, 0], [3, 1.32, 0]], [0.0536479, [3, -1.32, 0], [3, 0.68, 0]], [-0.0966839, [3, -0.68, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0, 3.96, 6])
    keys.append([[0.0183661, [3, -0.0133333, 0], [3, 1.32, 0]], [0.0199001, [3, -1.32, -0.00153397], [3, 0.68, 0.000790227]], [0.049046, [3, -0.68, 0], [3, 0, 0]]])

    tts.say("Now we will do the side lunge exercise.")
    tts.say("Slowly shift your weight to the side.")

    time.sleep(0.5)
    tts.say("Watch your balance.")

    time.sleep(1.0)
    tts.say("Keep your leg straight.")

    time.sleep(1.2)
    tts.say("Now back up.")

    # motion.angleInterpolation(names, keys, times, True)
    motion.angleInterpolationBezier(names, times, keys)

    time.sleep(1.5)
    tts.say("Well done! That was a strong side lunge.")

    return
