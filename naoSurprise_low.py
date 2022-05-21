# -*- encoding: UTF-8 -*-


def Surprise_low(IP):
    from naoqi import ALProxy
    import time
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([-0.195477, -0.195477, -0.195477, -0.195477, -0.195477, -0.195477, -0.195477, -0.195477, -0.195477, -0.195477, -0.195477, -0.195477, -0.195477, -0.195477, -0.195477, 0])

    names.append("RShoulderPitch")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([0.2, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6])

    names.append("RShoulderRoll")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([0.1, 0.2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3])

    names.append("RElbowRoll")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([0.0349, 0.25, 0.5, 1, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5])

    names.append("RElbowYaw")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([-0.075, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9])

    names.append("RWristYaw")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([0.75, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5])

    names.append("RHand")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])

    try:
        tts = ALProxy("ALTextToSpeech", IP, 9559)
        motion = ALProxy("ALMotion", IP, 9559)
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

            "ChestBoard/Led/Red/Actuator/Value"
        ]
        leds.createGroup("MyGroup", lednames)
        # time.sleep(10)

        leds.off("MyGroup")
        motion.angleInterpolation(names, keys, times, True, _async=True)
        motion.setStiffnesses("Body", 1.0) # stiffnesses=1.0
        leds.on("MyGroup")
    except BaseException, err:
        print err