#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    pub = rospy.Publisher('notchatter', String, queue_size=10)
    b = data.data + " robocon" 
    print(b)
    pub.publish(b)

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    hello_str = "hello world %s" % rospy.get_time()
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()

def listener():

    rospy.Subscriber("chatter", String, callback)
    rate = rospy.Rate(10)
    rate.sleep()

if __name__ == '__main__':

    rospy.init_node('talker_and_listener', anonymous=False)

    while not rospy.is_shutdown():
        talker()
        listener()
