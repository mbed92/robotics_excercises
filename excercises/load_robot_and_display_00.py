import numpy as np
import robopy.base.model as model


def run(robot):

    a = np.transpose(np.asmatrix(np.linspace(1, -180, 500)))
    b = np.transpose(np.asmatrix(np.linspace(1, 180, 500)))
    c = np.transpose(np.asmatrix(np.linspace(1, 90, 500)))
    d = np.transpose(np.asmatrix(np.linspace(1, 450, 500)))
    e = np.asmatrix(np.zeros((500, 1)))
    command = np.concatenate((d, b, a, e, c, d), axis=1)

    # animate results
    robot.animate(stances=command, frame_rate=30, unit='deg')

