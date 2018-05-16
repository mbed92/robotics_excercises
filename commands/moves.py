import numpy as np

from robopy.base import pose


def type_check(robot, start, stop, convert="joints"):
    """
    Checks if points are SE3 or joints and compute desired output coordinates format.
    :param robot: robot for inverse kinematics
    :param start: start pose or joint positions
    :param stop: stop pose or joint positions
    :param convert: desired return type. Pick "se3" or "joints".
    :return: joint positions or pose of start and stop in proper type.
    """

    # type check
    assert (type(start) == pose.SE3 and type(stop) == pose.SE3) or \
           (type(start) == list and type(stop) == list)

    if str(convert).lower() == "joints":
        # if pose is specified - compute joints
        if type(start) == pose.SE3 and type(stop) == pose.SE3:
            start = np.transpose(robot.ikine(np.asmatrix(start.data[0])), axes=(1, 0)) * 180 / np.pi
            stop = np.transpose(robot.ikine(np.asmatrix(stop.data[0])), axes=(1, 0)) * 180 / np.pi
            start = np.array(start)
            stop = np.array(stop)
    elif str(convert).lower() == "se3":
        # if joints are specified - compute pose
        if type(start) == list and type(stop) == list:
            start = robot.fkine(np.asmatrix(start), unit='deg')
            stop = robot.fkine(np.asmatrix(stop), unit='deg')

    return start, stop


def move_j(robot, P1, P2, number_of_joints=6, path_length=100):

    # type check
    start, stop = type_check(robot, P1, P2, "joints")

    # dimensions check for joint movement
    assert start.shape[0] == number_of_joints
    assert stop.shape[0] == number_of_joints

    # prepare joint trajectory
    path = []
    for i in range(number_of_joints):

        joint_path = np.transpose(np.asmatrix(np.linspace(start[i], stop[i], path_length)))
        if i < 1:
            path = joint_path
        else:
            path = np.concatenate((path, joint_path), axis=1)

    return path


def move_lin(robot, P1, P2, number_of_joints=6, path_length=100):

    # type check
    start, stop = type_check(robot, P1, P2, "se3")

    # compute increment
    incremental_step = 10
    increment = (stop - start) / path_length
    increment = np.array(increment.data)

    # compute path
    current_pose = start.data
    path = []
    for i in range(int(path_length / incremental_step)):

        # compute joint increments
        next_pose = current_pose + increment

        joint_start = robot.ikine(np.asmatrix(current_pose[0].data)) * 180 / np.pi
        joint_stop = robot.ikine(np.asmatrix(next_pose[0].data)) * 180 / np.pi

        # compute movement on short range
        path_part = []
        for k in range(number_of_joints):
            joint_path = np.transpose(np.asmatrix(np.linspace(joint_start[0, k], joint_stop[0, k], incremental_step)))

            if k < 1:
                path_part = joint_path
            else:
                path_part = np.concatenate((path_part, joint_path), axis=1)

        # concatenate paths
        if i < 1:
            path = path_part
        else:
            path = np.concatenate((path, path_part), axis=1)

        # update pose
        current_pose = current_pose + increment

    return path
