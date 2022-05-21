#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use goToPosture Method"""
import qi
import argparse
import sys
import naoAnger_low, naoAnger_high, naoSurprise_low, naoSurprise_high, naoHappy_low, naoHappy_high

def main(session):
    """
    This example uses the goToPosture method.
    """
    # Get the service ALRobotPosture.
    posture_service = session.service("ALRobotPosture")

    posture_service.goToPosture("StandInit", 1.0)

    # ANGER(low)
    # naoAnger_low.Anger_low()
    # ANGER(high)
    # naoAnger_high.Anger_high()

    # HAPPY
    # naoExited.Exited()

    # Surprised(low)
    # naoSurprise_low.Surprise_low()
    # Surprised(high)
    naoSurprise_high.Surprise_high()

    posture_service.goToPosture("StandInit", 1.0)


    session.close()
    # If session is NOT close, prompt keep launching something.

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    main(session)