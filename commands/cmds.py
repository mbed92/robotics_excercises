import numpy as np


def move_j(start_joint_position, stop_joint_position, number_of_joints=6, path_length=500):

    # convert data to numpy matrices
    start_joint_position = np.array(start_joint_position, dtype=np.float32)
    stop_joint_position = np.array(stop_joint_position, dtype=np.float32)

    # dimensions check
    assert start_joint_position.shape[0] == number_of_joints
    assert stop_joint_position.shape[0] == number_of_joints

    # prepare joint trajectory
    path = []
    for i in range(number_of_joints):

        joint_path = np.transpose(np.asmatrix(np.linspace(start_joint_position[i], stop_joint_position[i], path_length)))

        if i < 1:
            path = joint_path
        else:
            path = np.concatenate((path, joint_path), axis=1)

    return path
