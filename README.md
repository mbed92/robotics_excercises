# robotics_excercises
Forward kinematics excecises for robotics class in Python 3.5. Contol Engineering and Robotics, Electrical Faculty, 2018.

# Dependencies
Install dependencies using pip3:
* robopy - transformations, robots, forward and inverse kinematics, etc.
* vtk - visualization library
* numpy - numerical computing

# HOWTO:
Yo have two options:
* Run program in command line. In place of <robot_name> type _puma_ or _orion_
In case of orion remember that you have to adjust default code: python main.py <robot_name>

* Run program from PyCharm. Remember to set parameters in Edit Configurations.

# Excercises
Edit excercises which can be found in _excercises_ folder to solve problems and propose solutions. In _main.py_ remember to change the function to be executed.

## 00. Load robot
Just load and display two types of robot.

## 01. Joint move
Create paths using point-to-point move. Concatenate sub-paths.

## 02. Linear move
Create paths using linear move. Concatenate sub-paths. Notice the influence of precision of interpolation.

## 03. Playground
Create pick and place movement using point-to-point and linear moves.
