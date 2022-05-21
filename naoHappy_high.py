# -*- encoding: UTF-8 -*-

def Happy_high(IP):
    from naoqi import ALProxy
    import time
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([-0.15, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3])

    names.append("RShoulderPitch")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([-0.3, -0.6, -0.9, -1.2, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3])

    names.append("RShoulderRoll")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15])

    names.append("RElbowRoll")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([0.0349, 0.0349, 0.0349, 0.0349, 0.0349, 0.0349, 0.0349, 0.0349, 0.0349, 0.0349, 0.0349, 0.0349, 0.0349, 0.0349, 0.0349, 0.0349])

    # names.append("RWristYaw")
    # times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    # keys.append([0.5, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1])

    names.append("RHand")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    # left arm
    names.append("LShoulderPitch")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([-0.3, -0.6, -0.9, -1.2, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3])

    names.append("LShoulderRoll")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([-0.15, -0.15, -0.15, -0.15, -0.15, -0.15, -0.15, -0.15, -0.15, -0.15, -0.15, -0.15, -0.15, -0.15, -0.15, -0.15])

    names.append("LElbowRoll")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([-0.0349, -0.0349, -0.0349, -0.0349, -0.0349, -0.0349, -0.0349, -0.0349, -0.0349, -0.0349, -0.0349, -0.0349, -0.0349, -0.0349, -0.0349, -0.0349])

    # names.append("LWristYaw")
    # times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    # keys.append([-0.5, -1.1, -1.1, -1.1, -1.1, -1.1, -1.1, -1.1, -1.1, -1.1, -1.1, -1.1, -1.1, -1.1, -1.1, -1.1])

    names.append("LHand")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    try:
        motion = ALProxy("ALMotion", IP, 9559)
        tts = ALProxy("ALTextToSpeech", IP, 9559)
        leds = ALProxy("ALLeds", IP, 9559)
        lednames = [  # 양 눈깔
            "Face/Led/Red/Left/0Deg/Actuator/Value",
            "Face/Led/Red/Left/45Deg/Actuator/Value",
            "Face/Led/Red/Left/90Deg/Actuator/Value",
            "Face/Led/Red/Left/135Deg/Actuator/Value",
            "Face/Led/Red/Left/180Deg/Actuator/Value",
            "Face/Led/Red/Left/225Deg/Actuator/Value",
            "Face/Led/Red/Left/270Deg/Actuator/Value",
            "Face/Led/Red/Left/315Deg/Actuator/Value",

            "Face/Led/Red/Right/0Deg/Actuator/Value",
            "Face/Led/Red/Right/45Deg/Actuator/Value",
            "Face/Led/Red/Right/90Deg/Actuator/Value",
            "Face/Led/Red/Right/135Deg/Actuator/Value",
            "Face/Led/Red/Right/180Deg/Actuator/Value",
            "Face/Led/Red/Right/225Deg/Actuator/Value",
            "Face/Led/Red/Right/270Deg/Actuator/Value",
            "Face/Led/Red/Right/315Deg/Actuator/Value",

            "Face/Led/Blue/Left/0Deg/Actuator/Value",
            "Face/Led/Blue/Left/45Deg/Actuator/Value",
            "Face/Led/Blue/Left/90Deg/Actuator/Value",
            "Face/Led/Blue/Left/135Deg/Actuator/Value",
            "Face/Led/Blue/Left/180Deg/Actuator/Value",
            "Face/Led/Blue/Left/225Deg/Actuator/Value",
            "Face/Led/Blue/Left/270Deg/Actuator/Value",
            "Face/Led/Blue/Left/315Deg/Actuator/Value",

            "Face/Led/Blue/Right/0Deg/Actuator/Value",
            "Face/Led/Blue/Right/45Deg/Actuator/Value",
            "Face/Led/Blue/Right/90Deg/Actuator/Value",
            "Face/Led/Blue/Right/135Deg/Actuator/Value",
            "Face/Led/Blue/Right/180Deg/Actuator/Value",
            "Face/Led/Blue/Right/225Deg/Actuator/Value",
            "Face/Led/Blue/Right/270Deg/Actuator/Value",
            "Face/Led/Blue/Right/315Deg/Actuator/Value",

            "ChestBoard/Led/Red/Actuator/Value",
            "ChestBoard/Led/Blue/Actuator/Value"
        ]
        leds.createGroup("MyGroup", lednames)
        time.sleep(10)

        leds.off("MyGroup")
        motion.angleInterpolation(names, keys, times, True, _async=True)
        motion.setStiffnesses("Body", 1.0) # stiffnesses=1.0
        leds.on("MyGroup")
    except BaseException, err:
        print err