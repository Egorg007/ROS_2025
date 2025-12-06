#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64, Float64MultiArray

def process(msg):
    nums = msg.data
    s = sum(nums)
    pub.publish(Float64(s))
    rospy.loginfo(f"[summing] in={nums}  ->  out={s}")

rospy.init_node("summing")
pub = rospy.Publisher("result", Float64, queue_size=10)
sub = rospy.Subscriber("processed", Float64MultiArray, process)  # правильный топик

rospy.spin()

