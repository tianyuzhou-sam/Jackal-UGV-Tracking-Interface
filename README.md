# Jackal-Tracking-Interface
This GitHub repo is a waypoint tracking interface for [Clearpath Jackal UGV](https://clearpathrobotics.com/jackal-small-unmanned-ground-vehicle/). Please refer to the official [tutorial](https://www.clearpathrobotics.com/assets/guides/melodic/jackal/index.html#). **Jackal-Tracking-Interface** is able to obtain state estimation from motion capture systems [Qualisys](https://www.qualisys.com/), and you're welcome to write functions for your own motion capture system. The purpose of this repository is that prople can foucs on motion planning / path planning / trajectory planning and **Jackal-Tracking-Interface** can take over actual waypoint tracking as long as your planner outputs waypoints as csv files in a specific directory.

Dependencies
============
```
Python >= 3.8
numpy
transforms3d
matplotlib
```
And other dependencies for motion capture system.

Directory Initialization
========================

Assume you are currently under the main directory of this repository, then create two directories by
```
$ cd <MAIN_DIRECTORY>/experiment
$ mkdir traj
```

* The directory `/experiment/traj` stores the real trajectories (csv files) captured from Mocap system.
* The `waypoints.csv` file is stored in `/experiment`.


Communication between motion capture system and Jackal UGV
==========================================================

**Jackal-UGV-Tracking-Interface** utilizes motion capture system to obstain state estimation (positions and attitudes). **Jackal-UGV-Tracking-Interface** utilizes [TCP/IP](https://github.com/zehuilu/Tutorial-About-TCP-IP-and-UDP-Communications) communication to connect [motion capture system](https://github.com/zehuilu/How-to-Use-Qualisys-Motion-Capture-System)

How a waypoints/trajectory csv file looks like?
=====================================

The `waypoints.csv` can be read in real-time. When this file is overwrited, the future waypoints can be updated, that is, all waypoints with index number larger than the current waypoint's index can be updated during the task.

The file is constructed as:

[[  px0, py0 ]

 [  px1, py1 ]

 [  px2, py2 ]

      ...     ]

The files in `/experiment/traj` stores the real trajectories in the following structure:

[[    time     ]

 [  x position ]

 [  y position ]

 [   heading   ]

 [ linear velocity ]

 [ angular velocity ]]

How to run this interface
=========================

1. Run Jackal for a pre-specified set of waypoints
```
cd <MAIN_DIRECTORY>
python3 experiment/run_waypoints.py
```

2. Run Jackal with waypoints from file (can be updated in real-time)
```
cd <MAIN_DIRECTORY>
python3 experiment/run_Waypoints_from_file.py
```