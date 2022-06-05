# -*- encoding: UTF-8 -*-
def Anger_low(IP):
    from naoqi import ALProxy
    import time
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([0.05, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, -0.1])

    names.append("RShoulderRoll")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append(
        [0.3142, 0.3142, 0.3142, 0.3142, 0.3142, 0.3142, 0.3142, 0.3142, 0.3142, 0.3142, 0.3142, 0.3142, 0.3142, 0.3142,
         0.3142, 0.3142])

    names.append("RShoulderPitch")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append(
        [-0.175, -0.175, -0.175, -0.175, -0.175, -0.175, -0.175, -0.175, -0.175, -0.175, -0.175, -0.175, -0.175, -0.175,
         -0.175, -0.175])

    names.append("RElbowRoll")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append(
        [0.0349, 0.0349, 0.0349, 0.0349, 0.0349, 0.0349, 0.0349, 0.0349, 0.0349, 0.0349, 0.0349, 0.0349, 0.0349, 0.0349,
         0.0349, 0.0349])

    names.append("RWristYaw")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([-1.4, -1.4, -1.4, -1.4, -1.4, -1.4, -1.4, -1.4, -1.4, -1.4, -1.4, -1.4, -1.4, -1.4, -1.4, -1.4])

    names.append("LHand")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    names.append("RHand")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])

    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        motion = ALProxy("ALMotion", IP, 9559)
        leds = ALProxy("ALLeds", IP, 9559)
        Angerlow_leds = [
            "Face/Led/Green/Left/0Deg/Actuator/Value",
            "Face/Led/Green/Left/45Deg/Actuator/Value",
            "Face/Led/Green/Left/90Deg/Actuator/Value",
            "Face/Led/Green/Left/135Deg/Actuator/Value",
            "Face/Led/Green/Left/180Deg/Actuator/Value",
            "Face/Led/Green/Left/225Deg/Actuator/Value",
            "Face/Led/Green/Left/270Deg/Actuator/Value",
            "Face/Led/Green/Left/315Deg/Actuator/Value",

            "Face/Led/Green/Right/0Deg/Actuator/Value",
            "Face/Led/Green/Right/45Deg/Actuator/Value",
            "Face/Led/Green/Right/90Deg/Actuator/Value",
            "Face/Led/Green/Right/135Deg/Actuator/Value",
            "Face/Led/Green/Right/180Deg/Actuator/Value",
            "Face/Led/Green/Right/225Deg/Actuator/Value",
            "Face/Led/Green/Right/270Deg/Actuator/Value",
            "Face/Led/Green/Right/315Deg/Actuator/Value",

            "ChestBoard/Led/Green/Actuator/Value"
        ]
        # leds.createGroup("MyGroup", Angerlow_leds)
        # time.sleep(10)
        #나 조금 화났어 말하기

        # leds.off("MyGroup")
        motion.angleInterpolation(names, keys, times, True)
        motion.setStiffnesses("Body", 1.0)
        # leds.on("MyGroup")
    except BaseException, err:
        print(err)