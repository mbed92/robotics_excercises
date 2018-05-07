# just display robot in 3D

import robopy.base.transforms as trans
import numpy as np


def run(robot):

    num_steps = 50

    # positions of camera
    a = np.transpose(np.asmatrix(np.linspace(1, -180, num_steps)))
    b = np.transpose(np.asmatrix(np.linspace(1, 180, num_steps)))
    c = np.transpose(np.asmatrix(np.linspace(1, 90, num_steps)))
    d = np.transpose(np.asmatrix(np.linspace(1, 450, num_steps)))
    e = np.asmatrix(np.zeros((num_steps, 1)))
    command = np.concatenate((d, b, a, e, c, d), axis=1)

    print(command)

    # animate results
    robot.animate(stances=command, frame_rate=30, unit='deg')

