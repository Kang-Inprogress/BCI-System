# -*- encoding: UTF-8 -*-
def Anger_high(IP):
    from naoqi import ALProxy
    import time

    names = list()
    times = list()
    keys = list()

    names.append("RShoulderPitch")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6])

    names.append("LShoulderPitch")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6])

    names.append("RShoulderRoll")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([-1.1, -1.1, -0.6, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3])

    names.append("LShoulderRoll")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([1.1, 1.1, 0.6, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, -0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3])

    names.append("RElbowRoll")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([0.3, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6])

    names.append("LElbowRoll")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([-0.3, -0.6, -0.6, -0.6, -0.6, -0.6, -0.6, -0.6, -0.6, -0.6, -0.6, -0.6, -0.6, -0.6, -0.6, -0.6])

    names.append("LElbowYaw")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([0.075, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15])

    names.append("RElbowYaw")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([-0.075, -0.15, -0.15, -0.15, -0.15, -0.15, -0.15, -0.15, -0.15, -0.15, -0.15, -0.15, -0.15, -0.15, -0.15, -0.15])

    names.append("LHipYawPitch")
    times.append([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    keys.append([-0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3])


    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        # motion = ALProxy("ALMotion", IP, 9559)

        motion = ALProxy("ALMotion", IP, 9559)
        leds = ALProxy("ALLeds", IP, 9559)
        Angerhigh_leds = [  # 양 눈깔
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

            "ChestBoard/Led/Green/Actuator/Value",
            "ChestBoard/Led/Blue/Actuator/Value"
        ]
        leds.createGroup("MyGroup", Angerhigh_leds)
        time.sleep(10)

        leds.off("MyGroup")
        # "나 화났어" 대사 추가
        motion.angleInterpolation(names, keys, times, True, _async=True)
        motion.setStiffnesses("Body", 1.0) # stiffnesses=1.0
        leds.on("MyGroup")

    except BaseException, err:
        print(err)