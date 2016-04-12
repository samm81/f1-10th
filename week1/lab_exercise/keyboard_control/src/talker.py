#!/usr/bin/env python

import rospy
from keyboard_control.msg import drive_values
from keyboard_control.msg import drive_param
from std_msgs.msg import Bool


"""
What you should do:
 1. Subscribe to the keyboard messages (If you use the default keyboard.py, you must subcribe to "drive_paramters" which is publishing messages of "drive_param")
 2. Map the incoming values to the needed PWM values
 3. Publish the calculated PWM values on topic "drive_pwm" using custom message drive_values
"""
def listener():
 rospy.init_node('listener', anonymous=False)
 rospy.Subscriber("drive_parameters", String, callback)
 rospy.spin()
 
def callback(data):
 rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
 
 
def talker():
 # publish to the drive_pwm topic
  pub = rospy.Publisher('drive_pwm', drive_values, queue_size=10)
  rospy.init_node('talker', anonymous=False)
  rate = rospy.Rate(100)
  
