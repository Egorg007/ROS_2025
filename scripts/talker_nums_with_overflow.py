#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node('talker_nums')
pub = rospy.Publisher('my_chat_topic', String, queue_size=10)
overflow = rospy.Publisher('overflow_topic', String, queue_size=10)
rate = rospy.Rate(10)


def start_talker_nums():
	msg = String()
	i = 0
	is_overflow = False
	time_first = rospy.get_time()
	while not rospy.is_shutdown():
		time_second = rospy.get_time()
		delta_time = (time_second-time_first)*1000
		
		if i > 100 and is_overflow == False:
			is_overflow = True
			i = 0
		
		if is_overflow == False:
			nums_str = f"num = {i} time = {delta_time} ms"
			rospy.loginfo(nums_str)
			msg.data = nums_str
			overflow.publish(msg)
		else:
			
			nums_str = f"num = {i} time = {delta_time} ms"
			rospy.loginfo(nums_str)
			msg.data = nums_str
			pub.publish(msg)
		
		time_first = rospy.get_time()
		i += 2
		rate.sleep()
try:
	start_talker_nums()
except (rospy.ROSInterruptException, KeyboardInterrupt):
	rospy.logerr('Exception catched')

