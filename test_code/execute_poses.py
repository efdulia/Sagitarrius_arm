import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import time  # Import the time module

def main():
    # Initialize the moveit_commander
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('moveit_python_interface', anonymous=True)

    # Create the MoveGroupCommander for the arm and gripper
    arm_group = moveit_commander.MoveGroupCommander("arm_group")
    gripper_group = moveit_commander.MoveGroupCommander("gripper_group")

    # Define your poses sequence
    poses_sequence = [
        "pick_candy",
        "open",
        "close",
        "deliver_candy",
        "open",
        "close"
    ]

    # Execute the sequence with a time gap
    for pose in poses_sequence:
        if pose in ["open", "close"]:
            # Handle gripper commands
            if pose == "open":
                gripper_group.set_named_target("open")
                gripper_group.go(wait=True)
            else:
                gripper_group.set_named_target("close")
                gripper_group.go(wait=True)
        else:
            # Handle arm poses
            arm_group.set_named_target(pose)
            arm_group.go(wait=True)

        # Wait for 10 seconds before the next movement
        time.sleep(10)

    # Shut down MoveIt cleanly
    moveit_commander.roscpp_shutdown()

if __name__ == '__main__':
    main()
