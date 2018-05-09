# Define two points - P1 and P2. Implement movement between two points.

import numpy as np
import robopy.base.transforms as tr
import robopy.base.pose as pose
from robopy.base.util import ctraj
from pybotics.predefined_models import PUMA560


def run(robot):

    p1 = pose.SO3()
    p2 = p1.Rx(45)

    traj = ctraj(p1.t_matrix(), p2.t_matrix(), 100)


    # specify initial position - default 0 angles in each joint
    # p1 = np.asmatrix([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    # p2 = np.asmatrix([0.0, 0.0, 0.0, np.pi/2, 0.0, 0.0])
    #
    # num_steps =
    #
    # path = np.concatenate([p1, p2], axis=1)
    #
    # animate robot
    # robot.animate(stances=traj, frame_rate=30, unit='deg')



# def run(robot):
#
#     robot = PUMA560()
#     np.set_printoptions(suppress=True)
#
#     joints = np.deg2rad([10, 20, 30, 40, 50, 60])
#     pose = robot.fk(joints)
