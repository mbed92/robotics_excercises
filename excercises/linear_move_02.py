# Define two points - P1 and P2. Implement move_lin between two points.

import numpy as np

from robopy.base import pose
from robopy import rpy2r
from commands.moves import move_lin, move_j


def run(robot):

    rot1 = rpy2r([0, 0, 0], unit='deg')
    tran1 = [0.0, 0.0, 0.0]
    start = pose.SE3(tran1[0], tran1[1], tran1[2], rot1)
    print(start)

    rot2 = rpy2r([0, 0, 0], unit='deg')
    tran2 = [0.0, 0.5, 0.0]
    stop = pose.SE3(tran2[0], tran2[1], tran2[2], rot2)
    print(stop)

    # plot poses if needed
    # pose.SE3(tran1[0], tran1[1], tran1[2], rot1).plot()
    # pose.SE3(tran2[0], tran2[1], tran2[2], rot2).plot()

    path = move_lin(robot, start, stop)

    # animate robot
    robot.animate(stances=path, frame_rate=30, unit='deg')
