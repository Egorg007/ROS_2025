#!/usr/bin/env python3
import rospy
import datetime

def timeGainer():
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(0.2) # 10hz
	while not rospy.is_shutdown():
		readable_time = datetime.datetime.fromtimestamp(rospy.get_time()).strftime("%Y-%m-%d %H:%M:%S")
		rospy.loginfo("Time: %s" % readable_time)
		rate.sleep()

if __name__ == '__main__':
	try:
		timeGainer()
	except rospy.ROSInterruptException:
		pass
		

