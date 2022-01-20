#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_srvs.srv import Empty
from turtlesim.srv import TeleportAbsolute
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import time
import math


x=0
y=0
yaw=0
tolerance=0.001
deg=math.pi/2

def poseCallback(pose_message):
	global x,y,yaw
	x = pose_message.x
	y = pose_message.y
	yaw = pose_message.theta
	#print(x,y,yaw)

def vel_parametr(vel, lx=0, ly=0, lz=0, ax=0, ay=0, az=0):
	vel.linear.x = lx
	vel.linear.y = ly
	vel.linear.z = lz

	vel.angular.x = ax
	vel.angular.y = ay
	vel.angular.z = az
	return vel

def move (line_vel, ang_vel, dist):
	vel = Twist()
	rospy.init_node('turtmove', anonymous=True)
	cmd_vel_topic = '/turtle1/cmd_vel'
	vel_pub =rospy.Publisher (cmd_vel_topic, Twist, queue_size=10)
	#rospy.init_node('turt_pose', anonymous=True)
	position_topic ="/turtle1/pose"
	pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
	global x,y, yaw
	loop_rate = rospy.Rate(100)
	while not rospy.is_shutdown():
		pose_subscriber
		time.sleep(0.1)
		loop_rate.sleep()
		x0=x
		y0=y
		yaw0=yaw
		print(yaw*180/math.pi)
		distance_moved = 0.0
		angle_rotated = 0
		while (distance_moved<dist-tolerance):
			pose_subscriber
			time.sleep(0.1)
			vel_pub.publish(vel_parametr(vel, lx=line_vel))
			loop_rate.sleep()
			distance_moved=distance_moved+math.sqrt((x-x0)**2+(y-y0)**2)
		vel_pub.publish(vel_parametr(vel, ax=0))
		print(distance_moved)
		time.sleep(0.1)
		while (angle_rotated<deg-tolerance*1):
			pose_subscriber
			#print(yaw*180/math.pi)
			#time.sleep(0.1)
			#loop_rate.sleep()
			vel_pub.publish(vel_parametr(vel, az=ang_vel))
			loop_rate.sleep()
			angle_rotated = abs(yaw-yaw0)
		vel_pub.publish(vel_parametr(vel, az=0))
		#print (angle_rotated*180/math.pi)

if __name__ == '__main__':
	move(2.0, 1.5, 2)


