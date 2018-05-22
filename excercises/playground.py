# Define two points - P1 and P2. Implement move_lin between two points.

import numpy as np

from robopy.base import pose
from robopy import rpy2r
from commands.moves import move_lin, move_j


def run(robot):

    # start pose
    rot1 = rpy2r([0, 0, 0], unit='deg')
    tran1 = [0.5, 0.5, 0.5]
    start = pose.SE3(tran1[0], tran1[1], tran1[2], rot1)

    # auxiliary poses
    rot2 = rpy2r([0, 0, 0], unit='deg')
    tran2 = [0.1, 0.1, 0.0]
    mid = pose.SE3(tran2[0], tran2[1], tran2[2], rot2)
    mid2 = pose.SE3(tran2[0], tran2[1], tran2[2]+0.5, rot2)

    # final pose
    rot3 = rpy2r([0, 0, 0], unit='deg')
    tran3 = [0.1, 0.1, 0.0]
    stop = pose.SE3(tran3[0], tran3[1], tran3[2], rot3)

    # compute movements
    path1 = move_j(robot, start, mid)
    path2 = move_lin(robot, mid, mid2)
    path3 = move_j(robot, mid2, stop)

    # print size of paths
    print(path1.shape)
    print(path2.shape)
    print(path3.shape)

    # create final path
    path = np.concatenate((path1, path2, path3), axis=0)

    # animate robot
    robot.animate(stances=path, frame_rate=30, unit='deg')
