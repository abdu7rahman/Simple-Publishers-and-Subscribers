#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TalkerAndListener(Node):
    def __init__(self):
        super().__init__('talker_and_listener')
        self.publisher_chatter = self.create_publisher(String, 'chatter', 10)
        self.publisher_notchatter = self.create_publisher(String, 'notchatter', 10)

        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.callback,
            10
        )
        self.subscription  
        self.timer = self.create_timer(0.1, self.talker_callback)  # 10 Hz

    def talker_callback(self):
        hello_str = f"hello world "
        self.get_logger().info(f"Publishing to chatter: {hello_str}")
        msg = String()
        msg.data = hello_str
        self.publisher_chatter.publish(msg)

    def callback(self, msg):
        self.get_logger().info(f"I heard: {msg.data}")
        modified_data = f"{msg.data} robocon"
        print(modified_data) 
        
        new_msg = String()
        new_msg.data = modified_data
        self.publisher_notchatter.publish(new_msg)
        self.get_logger().info(f"Published to notchatter: {modified_data}")


def main(args=None):
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

