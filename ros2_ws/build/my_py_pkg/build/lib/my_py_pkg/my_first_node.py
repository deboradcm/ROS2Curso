#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)
    node = Node("py_test")
    node.get_logger().info("Hello Ros2")
    rclpy.spin(node)   #pausara o programa e permitirá que o nó continue

    rclpy.shutdown()

if __name__ == "__main__":
    main()