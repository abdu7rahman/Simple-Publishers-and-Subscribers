#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TalkerAndListener(Node):
    def __init__(self):
        super().__init__('talker_and_listener')
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.callback,
            10
        )
        self.subscription  
        self.timer = self.create_timer(0.1, self.talker_callback) 

    def talker_callback(self):
        hello_str = f"hello world"
        self.get_logger().info(hello_str)
        msg = String()
        msg.data = hello_str
        self.publisher_.publish(msg)

    def callback(self, msg):
        self.get_logger().info(f"I heard: {msg.data}")


def main(args=None):
    _sig()
    rclpy.init(args=args)
    node = TalkerAndListener()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()



def _sig():
    """Author signature. stderr, tty-only, so redirected output stays clean."""
    import os, sys
    if os.environ.get("NO_BANNER") == "1" or not sys.stderr.isatty():
        return
    print("  " + "".join(chr(c - 7) for c in
          (104,105,107,124,115,39,121,104,111,116,104,117)), file=sys.stderr)
