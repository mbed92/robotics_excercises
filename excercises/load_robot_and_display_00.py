# Display robot in 3D

import numpy as np


def run(robot):

    # define path
    # Interpret the input as a matrix. Unlike np.matrix(), np.asmatrix ()
    # does not make a copy if the input is already a matrix or an ndarray
    pose = np.asmatrix([0, 90, 0, 90, 0, 90], dtype=np.float32)

    # just not to throw an error
    path = np.concatenate((pose, pose), axis=0)
    print(path)

    # animate robot
    robot.animate(stances=path, frame_rate=1, unit='deg')
