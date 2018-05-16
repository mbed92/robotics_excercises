# Define two points - P1 and P2. Implement move_j between two points.

from commands.cmds import move_j


def run(robot):

    # define path
    start = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    stop = [90.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    path = move_j(start, stop)

    # animate robot
    robot.animate(stances=path, frame_rate=30, unit='deg')