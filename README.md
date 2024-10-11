## Sagittarius Arm Robot Simulation

This guide explains how to set up and run the Sagittarius Arm Robot simulation using ROS. Please follow the instructions carefully to ensure proper configuration of your environment.

# 1. Cloning the Repository

To get started, please navigate to the directory where you want to clone this repository. Clone the repository containing the necessary files into your workstation. In this example, I am working in `~/sagittarius_ws`, but you should replace this path with the location where you want to set up the files on your workstation.

```bash
cd ~/sagittarius_ws/src/  # Replace with your own directory if different
source devel/setup.bash
git clone https://github.com/efdulia/sagittarius_arm_ros_esrat.git
```

# 2. Launching the Customized Package

Next, launch the customized "sagittarius_moveit_Esrat_sim" package to visualize the arm robot in RViz.

```bash
roslaunch sagittarius_moveit_Esrat_sim demo.launch
```

# 3. Running the Python Script for Robot Arm Movement

After launching the RViz simulation, you can control the robot arm’s movements using a Python script located in the `test_code` folder.

To do this, open a new terminal and run the following commands:

```bash
cd ~/sagittarius_ws  # Replace with your own directory if different
source devel/setup.bash
cd src/sagittarius_arm_ros_esrat/test_code/
python3 execute_poses.py
```

Check the RViz that you launched. It should display the planning as instructed in the Python script.


