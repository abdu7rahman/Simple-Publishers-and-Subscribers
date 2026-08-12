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
    _sig()
    nonchatternode()


def _sig():
    """Author signature. stderr, tty-only, so redirected output stays clean."""
    import os, sys
    if os.environ.get("NO_BANNER") == "1" or not sys.stderr.isatty():
        return
    print("  " + "".join(chr(c - 7) for c in
          (104,105,107,124,115,39,121,104,111,116,104,117)), file=sys.stderr)
