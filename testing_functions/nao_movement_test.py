# import naoqi
# from naoqi import ALProxy

# motion = ALProxy("ALMotion", "nao.local", 9559)
# motion.setStiffnesses("Body", 1.0)

# #To make NAO walk, you should use ALMotionProxy::moveInit() (to put the robot in a correct position), and then ALMotionProxy::moveTo()
# motion.moveInit()
# motion.moveTo(0.5, 0, 0)


# motion = ALProxy("ALMotion", "nao.local", 9559)
# tts    = ALProxy("ALTextToSpeech", "nao.local", 9559)
# motion.moveInit()
# motion.post.moveTo(0.5, 0, 0)
# tts.say("I'm walking")

# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.24])
keys.append([-0.17])

names.append("HeadYaw")
times.append([0.24])
keys.append([0])

names.append("LAnklePitch")
times.append([0.24])
keys.append([0.0770168])

names.append("LAnkleRoll")
times.append([0.24])
keys.append([-0.0934085])

names.append("LElbowRoll")
times.append([0.24])
keys.append([-0.550405])

names.append("LElbowYaw")
times.append([0.24])
keys.append([-1.19494])

names.append("LHand")
times.append([0.24])
keys.append([0.316487])

names.append("LHipPitch")
times.append([0.24])
keys.append([0.177277])

names.append("LHipRoll")
times.append([0.24])
keys.append([0.0861374])

names.append("LHipYawPitch")
times.append([0.24])
keys.append([-0.159829])

names.append("LKneePitch")
times.append([0.24])
keys.append([-0.0857337])

names.append("LShoulderPitch")
times.append([0.24])
keys.append([1.48475])

names.append("LShoulderRoll")
times.append([0.24])
keys.append([0.207041])

names.append("LWristYaw")
times.append([0.24])
keys.append([0.102195])

names.append("RAnklePitch")
times.append([0.24])
keys.append([0.0768502])

names.append("RAnkleRoll")
times.append([0.24])
keys.append([0.107226])

names.append("RElbowRoll")
times.append([0.24])
keys.append([0.508891])

names.append("RElbowYaw")
times.append([0.24])
keys.append([1.29861])

names.append("RHand")
times.append([0.24])
keys.append([0.369505])

names.append("RHipPitch")
times.append([0.24])
keys.append([0.159447])

names.append("RHipRoll")
times.append([0.24])
keys.append([-0.118279])

names.append("RHipYawPitch")
times.append([0.24])
keys.append([-0.159829])

names.append("RKneePitch")
times.append([0.24])
keys.append([-0.0857337])

names.append("RShoulderPitch")
times.append([0.24])
keys.append([1.47445])

names.append("RShoulderRoll")
times.append([0.24, 0.92])
keys.append([-0.171881, -1.32645])

names.append("RWristYaw")
times.append([0.24])
keys.append([0.151052])

# try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
motion = ALProxy("ALMotion", "172.18.16.34", 9559)
#   motion = ALProxy("ALMotion")
motion.angleInterpolation(names, keys, times, True)
# except BaseException as err:
#   print err
