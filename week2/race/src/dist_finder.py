#!/usr/bin/env python

import rospy
import math
from sensor_msgs.msg import LaserScan
from race.msg import pid_input

desired_trajectory = 1
vel = 30

pub = rospy.Publisher('error', pid_input, queue_size=10)

## Input: data: Lidar scan data
## theta: The angle at which the distance is requried
## OUTPUT: distance of scan at angle theta
def getRange(data,theta):
    """ Find the index of the arary that corresponds to angle theta.
    Return the lidar scan value at that index
    Do some error checking for NaN and ubsurd values """

    thetap = math.radians(theta) + (3 * math.pi / 4)
    index = thetap / 0.004363
    d = data[index]
    return 

def callback(data):
	theta = 50;
	a = getRange(data,theta)
	b = getRange(data,0)
	swing = math.radians(theta)
	
        alpha = math.atan2( a * math.cos(theta) - b , a * math.sin(theta) )
        AB = b * math.cos(alpha)

        error = desired_trajectory - AB

	msg = pid_input()
	msg.pid_error = error
	msg.pid_vel = vel
	pub.publish(msg)
	

if __name__ == '__main__':
	print("Laser node started")
	rospy.init_node('dist_finder',anonymous = True)
	rospy.Subscriber("scan",LaserScan,callback)
	rospy.spin()
