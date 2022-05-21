# -*- encoding: UTF-8 -*-

def Happy_low(IP):
    from naoqi import ALProxy
    import time

    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([-0.1, -0.1, 0.1, 0.1, -0.1, -0.1, 0.1, 0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1])

    names.append("RShoulderPitch")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([0.15, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3])

    names.append("RShoulderRoll")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2])

    names.append("RElbowRoll")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3])

    names.append("RWristYaw")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([0.5, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1])

    names.append("RHand")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    # left arm
    # names.append("LShoulderPitch")
    # times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    # keys.append([0.15, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3])
    #
    # names.append("LShoulderRoll")
    # times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    # keys.append([-0.1, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2])
    #
    # names.append("LElbowRoll")
    # times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    # keys.append([-1.3, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3, -1.3])
    #
    # names.append("LWristYaw")
    # times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    # keys.append([-0.5, -1.1, -1.1, -1.1, -1.1, -1.1, -1.1, -1.1, -1.1, -1.1, -1.1, -1.1, -1.1, -1.1, -1.1, -1.1])
    #
    # names.append("LHand")
    # times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    # keys.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    try:
        tts = ALProxy("ALTextToSpeech", IP, 9559)
        motion = ALProxy("ALMotion", IP, 9559)
        leds = ALProxy("ALLeds", IP, 9559)
        ledNames = [  # 양 눈깔
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

            "ChestBoard/Led/Blue/Actuator/Value"
        ]
        leds.createGroup("EyesChestLeds", ledNames)
        time.sleep(10)

        leds.off("EyesChestLeds")

        # tts.say("아!", _async=True)
        motion.angleInterpolation(names, keys, times, True, _async=True)
        motion.setStiffnesses("Body", 1.0) # stiffnesses=1.0
        leds.on("EyesChestLeds")
    except BaseException, err:
        print err