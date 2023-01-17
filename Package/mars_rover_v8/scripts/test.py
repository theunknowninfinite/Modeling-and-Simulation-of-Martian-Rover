#!/usr/bin/env python3

# from sympy import true
import rospy
from std_msgs.msg import Float64
import time

rospy.init_node('arm_control')
Arm_base = rospy.Publisher('/mars_rover_v8/Arm_base_joint_controller/command', Float64, queue_size=10)
Arm_link2= rospy.Publisher('/mars_rover_v8/Arm_link2_joint_controller/command', Float64, queue_size=10)
Arm_link4= rospy.Publisher('/mars_rover_v8/Arm_link4_joint_controller/command', Float64, queue_size=10)
End_effector= rospy.Publisher('/mars_rover_v8/End_effector_joint_controller/command', Float64, queue_size=10)
# Wheel Control
Left_rear_wheel = rospy.Publisher('/mars_rover_v8/Left_rear_wheel_link_joint_controller/command', Float64, queue_size=10)
Left_middle_wheel = rospy.Publisher('/mars_rover_v8/Left_middle_wheel_link_joint_controller/command', Float64, queue_size=10)
Left_front_wheel = rospy.Publisher('/mars_rover_v8/Left_front_wheel_link_joint_controller/command', Float64, queue_size=10)
Right_rear_wheel =  rospy.Publisher('/mars_rover_v8/Right_rear_wheel_link_joint_controller/command', Float64, queue_size=10)
Right_middle_wheel =  rospy.Publisher('/mars_rover_v8/Right_middle_wheel_link_joint_controller/command', Float64, queue_size=10)
Right_front_wheel =  rospy.Publisher('/mars_rover_v8/Right_front_wheel_link_joint_controller/command', Float64, queue_size=10)
# Steering Control
Left_rear_wheel_shaft = rospy.Publisher('/mars_rover_v8/Left_rear_wheel_shaft_joint_controller/command', Float64, queue_size=10)
Right_rear_wheel_shaft =  rospy.Publisher('/mars_rover_v8/Right_rear_wheel_shaft_joint_controller/command', Float64, queue_size=10)
Left_front_wheel_shaft =  rospy.Publisher('/mars_rover_v8/Left_front_wheel_shaft_joint_controller/command', Float64, queue_size=10)
Right_front_wheel_shaft =  rospy.Publisher('/mars_rover_v8/Right_front_wheel_shaft_joint_controller/command', Float64, queue_size=10)
# Suspension control
Main_RBL_shaft = rospy.Publisher('/mars_rover_v8/Main_RBL_shaft_joint_controller/command', Float64, queue_size=10)
Main_RBR_shaft =  rospy.Publisher('/mars_rover_v8/Main_RBR_shaft_joint_controller/command', Float64, queue_size=10)
RBL_sub =  rospy.Publisher('/mars_rover_v8/RBL_sub_joint_controller/command', Float64, queue_size=10)
RBR_sub =  rospy.Publisher('/mars_rover_v8/RBR_sub_joint_controller/command', Float64, queue_size=10)
rate = rospy.Rate(10)

# # Init Messages
# Left_rear_wheel_velocity_msg = Float64()
# Left_middle_wheel_velocity_msg = Float64()
# Left_front_wheel_velocity_msg = Float64()
# Right_rear_wheel_velocity_msg = Float64()
# Right_middle_wheel_velocity_msg = Float64()
# Right_front_wheel_velocity_msg = Float64()
# Main_RBL_shaft_pos_msg = Float64()
# Main_RBR_shaft_pos_msg = Float64()
# RBL_sub_pos_msg = Float64()
# RBR_sub_pos_msg = Float64()
# Left_rear_wheel_shaft_pos_msg = Float64()
# Right_rear_wheel_shaft_pos_msg = Float64()
# Left_front_wheel_shaft_pos_msg = Float64()
# Right_front_wheel_shaft_pos_msg = Float64()


def test_fn(number):
    
    if number==1:
        for i in range(100):
            Left_rear_wheel.publish(-1)
            Left_middle_wheel.publish(-1)
            Left_front_wheel.publish(-1)
            Right_rear_wheel.publish(1)
            Right_middle_wheel.publish(1)
            Right_front_wheel.publish(1)
            rate.sleep()
        for i in range (10):  

            Left_rear_wheel.publish(0)
            Left_middle_wheel.publish(0)
            Left_front_wheel.publish(0)
            Right_rear_wheel.publish(0)
            Right_middle_wheel.publish(0)
            Right_front_wheel.publish(0)  

        Arm_base.publish(-110)
        Arm_link2.publish(-90)
        Arm_link4.publish(10)
        End_effector.publish(500)

    
    if number==2:

        Right_rear_wheel.publish(1)
        Right_middle_wheel.publish(1)
        Right_front_wheel.publish(1)

    if number==3:
        Left_rear_wheel_shaft.publish(0)
        Right_rear_wheel_shaft.publish(0)
        Left_front_wheel_shaft.publish(0)
        Right_front_wheel_shaft.publish(0)

    if number==4:

        Arm_base.publish(-90)
        Arm_link2.publish(-90)
        Arm_link4.publish(5)
        End_effector.publish(500)
    
    if number==5:
        Main_RBL_shaft.publish(0)
        Main_RBR_shaft.publish(0)
        RBL_sub.publish(0)
        RBR_sub.publish(0)

    if number ==0:

        Left_rear_wheel.publish(0)
        Left_middle_wheel.publish(0)
        Left_front_wheel.publish(0)
        Right_rear_wheel.publish(0)
        Right_middle_wheel.publish(0)
        Right_front_wheel.publish(0)
        Arm_base.publish(0)
        Arm_link2.publish(0)
        Arm_link4.publish(0)
        End_effector.publish(0)
        Main_RBL_shaft.publish(0)
        Main_RBR_shaft.publish(0)
        RBL_sub.publish(0)
        RBR_sub.publish(0)


if __name__ == '__main__':
    try:
        inout=int(input("Enter Number "))
        test_fn(inout)
    except rospy.ROSInterruptException:
        pass