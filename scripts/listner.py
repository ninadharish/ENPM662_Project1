#!/usr/bin/env python
import rospy

from std_msgs.msg import Float64

import sys, select, termios, tty

def callback(data):
   rospy.loginfo(rospy.get_caller_id() + "rear drive_control speed%s", data.data)

def callback2(data):
   rospy.loginfo(rospy.get_caller_id() + "left_control turn%s", data.data)

def callback3(data):
   rospy.loginfo(rospy.get_caller_id() + "right_control turn%s", data.data)

if __name__=="__main__":

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/mini_robot/rear_drive_controller/command", Float64, callback) 
    rospy.Subscriber("/mini_robot/left_front_steer_controller/command", Float64, callback2)
    rospy.Subscriber("/mini_robot/right_front_steer_controller/command", Float64, callback3)
    
    rospy.spin()
