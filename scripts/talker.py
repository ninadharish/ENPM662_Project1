#!/usr/bin/env python
import rospy

from std_msgs.msg import Float64

import sys, select, termios, tty


def talker():
    rospy.init_node('mini_robot_teleop')
    pub_right_1 = rospy.Publisher('/mini_robot/right_front_steer_controller/command', Float64, queue_size=10) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
    # pub_right_2 = rospy.Publisher('/mini_robot/left_front_steer_controller/command', Float64, queue_size=10)
    pub_left_1 = rospy.Publisher('/mini_robot/left_front_steer_controller/command', Float64, queue_size=10) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
    # pub_left_2 = rospy.Publisher('/mini_robot/right_front_steer_controller/command', Float64, queue_size=10)
    pub_move_1 = rospy.Publisher('/mini_robot/rear_drive_controller/command', Float64, queue_size=10) # Add your topic for move here '' Eg '/my_robot/longitudinal_controller/command'
    
    control_speed = -7
    control_turn = -0.5
    while(1):
        pub_right_1.publish(control_turn) # publish the turn command.
            # pub_right_2.publish(control_turn)
        pub_left_1.publish(control_turn) # publish the turn command.
            # pub_left_2.publish(control_turn)
        pub_move_1.publish(control_speed) # publish the control speed.

        rospy.loginfo(control_speed)
        rospy.loginfo(control_turn) 

if __name__=="__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
