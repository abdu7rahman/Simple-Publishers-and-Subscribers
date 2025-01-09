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

