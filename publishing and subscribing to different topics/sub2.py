#!/usr/bin/env python
import rospy
from std_msgs.msg import String
  
def callback(b):

    print(b.data)
    
def nonchatternode():

    rospy.init_node('nonchatternode', anonymous=False)

    rospy.Subscriber('notchatter', String, callback)

    rospy.spin()

if __name__ == '__main__':
    nonchatternode()
