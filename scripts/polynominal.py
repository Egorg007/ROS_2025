#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64MultiArray

def process(msg):
    result = [v ** (i+1) for i, v in enumerate(msg.data)]
    pub.publish(Float64MultiArray(data=result))
    rospy.loginfo(f"in={msg.data} -> out={result}")

rospy.init_node("polynominal")
pub = rospy.Publisher("processed", Float64MultiArray, queue_size=10)
sub = rospy.Subscriber("input", Float64MultiArray, process)  # исправлено

rospy.spin()

