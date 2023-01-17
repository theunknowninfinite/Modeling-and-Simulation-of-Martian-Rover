#!/usr/bin/env python3

# from sympy import true
import rospy
from std_msgs.msg import Float64
import time

rospy.init_node('arm_control')
link_1 = rospy.Publisher('/mars_rover_v8/Arm_base_joint_controller/command', Float64, queue_size=10)
link_2= rospy.Publisher('/mars_rover_v8/Arm_link2_joint_controller/command', Float64, queue_size=10)
link_3= rospy.Publisher('/mars_rover_v8/Arm_link4_joint_controller/command', Float64, queue_size=10)
link_4= rospy.Publisher('/mars_rover_v8/Drill_tool_joint_controller/command', Float64, queue_size=10)

# rospy.init_node('platform_straight')
move1 = rospy.Publisher('/mars_rover_v8/Left_rear_wheel_link_joint_controller/command', Float64, queue_size=10)
move2 = rospy.Publisher('/mars_rover_v8/Left_middle_wheel_link_joint_controller/command', Float64, queue_size=10)
move3 = rospy.Publisher('/mars_rover_v8/Left_front_wheel_link_joint_controller/command', Float64, queue_size=10)
move4 =  rospy.Publisher('/mars_rover_v8/Right_rear_wheel_link_joint_controller/command', Float64, queue_size=10)
move5 =  rospy.Publisher('/mars_rover_v8/Right_middle_wheel_link_joint_controller/command', Float64, queue_size=10)
move6 =  rospy.Publisher('/mars_rover_v8/Right_front_wheel_link_joint_controller/command', Float64, queue_size=10)

def arm_pose(theta1, theta2, d3):
    link_1.publish(theta1)
    link_2.publish(theta2)
    link_3.publish(d3)
    
    # r = rospy.Rate(10)

def platform():
    # r = rospy.Rate(10) 
    # print("Received velocity")
    
    # for i in range(100):
        move1.publish(-5.0)
        move2.publish(-5.0)
        move3.publish(5.0)
        move4.publish(-5.0)
        move5.publish(-5.0)
        move6.publish(5.0)
        link_4.publish(10.0)
    # r.sleep()
    # print("End velocity") 
    # move1.publish(0.0)
    # move2.publish(0.0)
    # move3.publish(0.0)
    # move4.publish(0.0)
    # move5.publish(0.0)
    # move6.publish(0.0)
    

# if __name__ == '__main__':
#     try:
platform()
arm_pose(0.50,0.0, 0.0)
time.sleep(5)
arm_pose(0.0, -2.70, -0.09)
# platform()
time.sleep(5)
    # except rospy.ROSInternalException:
        # pass
