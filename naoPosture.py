#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use goToPosture Method"""
import qi
import argparse
import sys
import naoAnger_low, naoAnger_high, naoSurprise_low, naoSurprise_high, naoHappy_low, naoHappy_high

def main(session):
    IP = args.ip
    now_emot = args.emot
    """
    This example uses the goToPosture method.
    """
    # Get the service ALRobotPosture.
    posture_service = session.service("ALRobotPosture")


    posture_service.goToPosture("StandInit", 1.0)

    if (now_emot == "anger_low"):
        naoAnger_low.Anger_low(IP)

    elif (now_emot == "anger_high"):
        naoAnger_high.Anger_high(IP)

    elif (now_emot == "surprise_low"):
        naoSurprise_low.Surprise_low(IP)

    elif (now_emot == "surprise_high"):
        naoSurprise_high.Surprise_high(IP)

    elif (now_emot == "happy_low"):
        naoHappy_low.Happy_low(IP)

    elif (now_emot == "happy_high"):
        naoHappy_high.Happy_high(IP)
    else:
        print("Error! emot is Neutral")
    posture_service.goToPosture("StandInit", 1.0)


    session.close()
    # If session is NOT close, prompt keep launching something.

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")
    parser.add_argument("--emot", type=str, default="neutral",
                        help="input emot")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    main(session)