# Display robot in 3D


def run(robot):

    # define path
    path = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    # animate robot
    robot.animate(stances=path, frame_rate=30, unit='deg')
