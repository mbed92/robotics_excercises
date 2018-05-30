# Define points. Implement move_j between them.

import numpy as np
from robopy.base import pose
from commands.moves import move_j


def run(robot):

    # define joint positions
    start = [0.0, 90.0, 0.0, 0.0, 0.0, 0.0]
    middle = [90.0, 90.0, 0.0, 0.0, 0.0, 0.0]
    stop = [90.0, 90.0, 30.0, 0.0, 0.0, 0.0]

    # compute path
    path1 = move_j(robot, start, middle)
    path2 = move_j(robot, middle, stop)

    # concatenate entire path
    path = np.concatenate((path1, path2), axis=0)
    print(path)

    # animate robot
    robot.animate(stances=path, frame_rate=30, unit='deg')
