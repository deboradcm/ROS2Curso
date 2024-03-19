class SmartphoneNode(Node):
    def __init__(self):
       super().__init__("smartphone")



def main(args=None):
    rclpy.init(args=args)
    node = SmartphoneNode()
    rclpy.spin(node)   
    rclpy.shutdown()

if __name__ == "__main__":
    main()