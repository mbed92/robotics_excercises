# built-in libraries
import argparse
import robopy.base.model as robot
import sys

# user libraries
from excercises import *

# argument parser
parser = argparse.ArgumentParser()
parser.add_argument("model", help="Model of robot (puma / orion)")
args = parser.parse_args()


# prepare main
def main():

    # load model
    if str(args.model).lower() == "puma":
        model = robot.Puma560()
    elif str(args.model).lower() == "orion":
        model = robot.Orion5()
    else:
        print("Bad model specified. Try again.")
        sys.exit()

    # start excercise
    load_robot_and_display_00.run(model)


# run main
if __name__ == '__main__':
    main()
