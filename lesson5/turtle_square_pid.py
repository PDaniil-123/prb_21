#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_srvs.srv import Empty
from turtlesim.srv import TeleportAbsolute
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import time
import math
import datetime

x=0
y=0
yaw=0
tolerance=0.0001
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

def move (dist):
	vel = Twist()
	P=5
	I=0.01
	D=0.1
	rospy.init_node('turtmove', anonymous=True)
	cmd_vel_topic = '/turtle1/cmd_vel'
	vel_pub =rospy.Publisher (cmd_vel_topic, Twist, queue_size=10)
	#rospy.init_node('turt_pose', anonymous=True)
	position_topic ="/turtle1/pose"
	pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
	global x,y, yaw
	loop_rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		#print('start')
		pose_subscriber
		time.sleep(0.1)
		x0=x
		y0=y
		yaw0=yaw
		#print(yaw*180/math.pi)
		dist_left=dist
		angle_left = deg
		t0=time.time()
		line_vel=2.0
		ang_vel=2.0
		lxI=0
		azI=0
		while (dist_left>tolerance):
			d=dist_left
			t1=time.time()
			vel_pub.publish(vel_parametr(vel, lx=line_vel))
			loop_rate.sleep()
			#
			pose_subscriber
			dist_left=dist-math.sqrt((x-x0)**2+(y-y0)**2)
			t2=time.time()
			lxP=dist_left*P
			lxI=lxI+dist_left*(t2-t1)*I
			lxD=(d-dist_left)/(t2-t1)*D
			line_vel=lxP+lxI+lxD
			#print(line_vel)
#		#print(dist_left)
		vel_pub.publish(vel_parametr(vel, ax=0))
#		time.sleep(5)
#		dist_left=dist-math.sqrt((x-x0)**2+(y-y0)**2)
#		print('goal is reached',dist_left)
		while ((angle_left)>tolerance):
			a=angle_left
			t1=time.time()
			vel_pub.publish(vel_parametr(vel, az=ang_vel))
			loop_rate.sleep()
			angle_left = deg-math.acos((math.cos(yaw0)*math.cos(yaw)+math.sin(yaw0)*math.sin(yaw)))
			#print(yaw,yaw0, angle_left*180/math.pi)
			t2=time.time()
			azP=angle_left*P
			azI=azI+angle_left*(t2-t1)*I
			azD=abs(a-angle_left)/(t2-t1)*D
			ang_vel=azP+azI+azD
		vel_pub.publish(vel_parametr(vel, az=0))
		

if __name__ == '__main__':
	move(2)


