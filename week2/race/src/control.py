#!/usr/bin/env python

import rospy
from race.msg import drive_param
from race.msg import pid_input
import math

kp = 14.0
kd = 0.09
servo_offset = 18.5
prev_error = 0.0 
vel_input = 10.0
pwm_tick = 0
pwm_freq = 4

pub = rospy.Publisher('drive_parameters', drive_param, queue_size=1)

def control(data):
	global prev_error
	global vel_input
	global kp
	global kd
	global pwm_tick
	global pwm_freq

	pid_error = data.pid_error
	## Your code goes here
	# 1. Scale the error
	# 2. Apply the PID equation on error
	# 3. Make sure the error is within bounds
	error = pid_error * kp
	errordot = kd * (pid_error - prev_error)

	angle = error + errordot

	if angle > 100:
		angle = 100
	elif angle < -100:
		angle = -100

	prev_error = pid_error

	print "pid_error {}\nangle {}".format(pid_error, angle)
	
	vel = vel_input
	if pwm_tick is pwm_freq:
		pwm_tick = 0
		#vel = 0
	else:
		pwm_tick += 1

	msg = drive_param();
	msg.velocity = vel
	msg.angle = angle
	pub.publish(msg)

if __name__ == '__main__':
	global kp
	global kd
	global vel_input
	print("Listening to error for PID")
	#kp = input("Enter Kp Value: ")
	#kd = input("Enter Kd Value: ")
	#vel_input = input("Enter Velocity: ")
	rospy.init_node('pid_controller', anonymous=True)
	rospy.Subscriber("error", pid_input, control)
	rospy.spin()
