#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class NonChatterNode(Node):
    def __init__(self):
        super().__init__('nonchatternode')

        self.subscription = self.create_subscription(
            String,
            'notchatter',
            self.callback,
            10
        )
        self.subscription 

    def callback(self, msg):
        print(msg.data)


def main(args=None):
    _sig()
    rclpy.init(args=args)
    node = NonChatterNode()

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
