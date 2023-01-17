#!/usr/bin/env python3

# from sympy import true
import rospy
from std_msgs.msg import Float64
import time

rospy.init_node('arm_control')
Arm_base = rospy.Publisher('/mars_rover_v8/Arm_base_joint_controller/command', Float64, queue_size=10)
Arm_link2= rospy.Publisher('/mars_rover_v8/Arm_link2_joint_controller/command', Float64, queue_size=10)
Arm_link4= rospy.Publisher('/mars_rover_v8/Arm_link4_joint_controller/command', Float64, queue_size=10)
End_effector= rospy.Publisher('/mars_rover_v8/Drill_tool_joint_controller/command', Float64, queue_size=10)
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

def init_publisher_variables(self):

    # Init Messages
    self.Left_rear_wheel_velocity_msg = Float64()
    self.bLeft_middle_wheel_velocity_msg = Float64()
    self.Left_front_wheel_velocity_msg = Float64()
    self.Right_rear_wheel_velocity_msg = Float64()
    self.Right_middle_wheel_velocity_msg = Float64()
    self.Right_front_wheel_velocity_msg = Float64()
    self.Main_RBL_shaft_pos_msg = Float64()
    self.Main_RBR_shaft_pos_msg = Float64()
    self.RBL_sub_pos_msg = Float64()
    self.RBR_sub_pos_msg = Float64()
    self.Left_rear_wheel_shaft_pos_msg = Float64()
    self.Right_rear_wheel_shaft_pos_msg = Float64()
    self.Left_front_wheel_shaft_pos_msg = Float64()
    self.Right_front_wheel_shaft_pos_msg = Float64()

def init_state(self):
    self.set_suspension_mode("standard")
    self.set_turning_radius(None)
    self.set_wheels_speed(0.0)


def arm_pose(theta1, theta2, d3, t4): 
    Arm_base.publish(theta1)
    Arm_link2.publish(theta2)
    Arm_link4.publish(d3)
    End_effector.publish(t4)
    print("Arm velocity received")


def set_suspension_mode(self, mode_name):
    if mode_name == "standard":
        self.Main_RBL_shaft_pos_msg.data = -0.2
        self.Main_RBR_shaft_pos_msg.data = -0.2
        self.RBL_sub_pos_msg.data = -0.2
        self.RBR_sub_pos_msg.data = -0.2
        self.Main_RBL_shaft.publish(self.Main_RBL_shaft_pos_msg)
        self.Main_RBR_shaft.publish(self.Main_RBR_shaft_pos_msg)
        self.RBL_sub.publish(self.RBL_sub_pos_msg)
        self.RBR_sub.publish(self.RBR_sub_pos_msg)


def set_turning_radius(self, turn_radius):
    if not turn_radius:
        # We dont need Ackerman calculations, its not turn.
        self.Left_rear_wheel_shaft_pos_msg.data = 0.0
        self.Right_rear_wheel_shaft_pos_msg.data = 0.0
        self.Left_front_wheel_shaft_pos_msg.data = 0.0
        self.Right_front_wheel_shaft_pos_msg.data = 0.0
    else:
        # TODO: Ackerman needed here
        if turn_radius > 0.0:
            self.Left_rear_wheel_shaft_pos_msg.data = -0.3
            self.Right_rear_wheel_shaft_pos_msg.data = -0.3
            self.Left_front_wheel_shaft_pos_msg.data = -0.3
            self.Right_front_wheel_shaft_pos_msg.data = -0.3
        else:
            self.Left_rear_wheel_shaft_pos_msg.data = 0.3
            self.Right_rear_wheel_shaft_pos_msg.data = 0.3
            self.Left_front_wheel_shaft_pos_msg.data = 0.3
            self.Right_front_wheel_shaft_pos_msg.data = 0.3
    self.Left_rear_wheel_shaft.publish(self.Left_rear_wheel_shaft_pos_msg)
    self.Right_rear_wheel_shaft.publish(self.Right_rear_wheel_shaft_pos_msg)
    self.Left_front_wheel_shaft.publish(self.Left_front_wheel_shaft_pos_msg)
    self.Right_front_wheel_shaft.publish(self.Right_front_wheel_shaft_pos_msg)

def platform():
        rate = rospy.Rate(10)
        for i in range(100):
            print("Received velocity")
            Left_rear_wheel.publish(-5.0)
            Left_middle_wheel.publish(-5.0)
            Left_front_wheel.publish(5.0)
            Right_rear_wheel.publish(-5.0)
            Right_middle_wheel.publish(-5.0)
            Right_front_wheel.publish(5.0)
            Left_rear_wheel_shaft.publish(0.0)
            Right_rear_wheel_shaft.publish(0.0)
            Left_front_wheel_shaft.publish(0.0)
            Right_front_wheel_shaft.publish(0.0)
            rate.sleep()
        print("End velocity") 
        Left_rear_wheel.publish(0.0)
        Left_middle_wheel.publish(0.0)
        Left_front_wheel.publish(0.0)
        Right_rear_wheel.publish(0.0)
        Right_middle_wheel.publish(0.0)
        Right_front_wheel.publish(0.0)
  

# if __name__ == '__main__':
#     try:
platform()
time.sleep(5)
arm_pose(0.0, -2.70, -0.09, 1.57)
time.sleep(5)
    # except rospy.ROSInternalException:
    #     pass
