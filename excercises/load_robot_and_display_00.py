# Display robot in 3D

import numpy as np


def run(robot):

    # specify initial position - default 0 angles in each joint
    path = np.array([[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])

    # animate robot
    robot.animate(stances=path, frame_rate=30, unit='deg')

