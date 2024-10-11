## Sagittarius Arm Robot Simulation

This guide explains how to set up and run the Sagittarius Arm Robot simulation using ROS. Please follow the instructions carefully to ensure proper configuration of your environment.

# Step 1. Cloning the Repository

To get started, navigate to the directory where you want to clone this repository. Clone the repository containing the necessary files into your workstation. If you installed the "sagittarius_ws" workspace from (https://github.com/NXROBO/sagittarius_ws), then follow the commands below:

```bash
cd ~/sagittarius_ws/src/  # Replace with your own directory if different
source devel/setup.bash
git clone https://github.com/efdulia/sagitarrius_arm_ros_esrat.git
```

# Step 2. Launching the Customized Package

Next, launch the customized "sagittarius_moveit_Esrat_sim" package to visualize the arm robot in RViz. This package contains the customized configuration and launch files created in the MoveIt Assistant. 

```bash
roslaunch sagittarius_moveit_Esrat_sim demo.launch
```

I have defined all the groups and poses for the arm here. You can add more poses if needed.

# Step 3. Adding More Poses

Please skip this step and go to step 4 if you don't want to add more poses and would like to explore the existing ones first.

To add more poses, open a new terminal and follow the commands below:

```bash
cd ~/sagittarius_ws    
source devel/setup.bash  
roslaunch moveit_setup_assistant setup_assistant.launch
```
This should open the MoveIt Assistant. Now click on "Edit Existing MoveIt Configuration Package" and browse to this path:
```bash
/home/your_username/sagittarius_ws/src/sagittarius_arm_ros_esrat/sagittarius_moveit_Esrat_sim
```
Go to the "Robot Poses" tab on the left, add more poses, and save them. After adding new poses in MoveIt Assistant, you only need to update the pose name in the "execute_poses" Python script. This is the script responsible for controlling the arm’s movements, as mentioned in step 4. Once updated, the script will use these new poses to command the robot arm in RViz.

# Step 4. Running the Python Script for Robot Arm Movement

After launching the RViz simulation, you can control the robot arm’s movements using a Python script named "execute_poses," located in the test_code folder.

To do this, open a new terminal and run the following commands:

```bash
cd ~/sagittarius_ws  # Replace with your own directory if different
source devel/setup.bash
cd src/sagittarius_arm_ros_esrat/test_code/
python3 execute_poses.py
```

Check the RViz that you launched. It should display the planning as instructed in the Python script.


