#!/usr/bin/env python3
import rospy
import sys
from std_msgs.msg import Float64MultiArray, Float64

rospy.init_node('request', anonymous=True)

nums = [float(arg) for arg in sys.argv[1:4]] if len(sys.argv) >= 4 else [1.0, 2.0, 3.0]

result_container = {'value': None}  # используем словарь вместо nonlocal

def result_cb(msg):
    result_container['value'] = msg.data
    rospy.loginfo(f"[request] received result: {msg.data}")

pub = rospy.Publisher('input', Float64MultiArray, queue_size=1)
sub = rospy.Subscriber('result', Float64, result_cb)

rospy.sleep(0.5)
pub.publish(Float64MultiArray(data=nums))
rospy.loginfo(f"[request] published numbers: {nums}, waiting for result...")

timeout = rospy.Time.now() + rospy.Duration(5)
rate = rospy.Rate(10)
while not rospy.is_shutdown() and result_container['value'] is None and rospy.Time.now() < timeout:
    rate.sleep()

if result_container['value'] is None:
    rospy.logwarn("[request] timeout waiting for result")
    sys.exit(1)

print(result_container['value'])

