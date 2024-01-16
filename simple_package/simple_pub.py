import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class Simple_pub(Node):
    def __init__(self):
        super().__init__("simple_pub")  # type: ignore
        self.create_timer(1, self.print_hellow)
        self.pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)

    def print_hellow(self):
        msg = Twist()
        msg.linear.x = 1.0
        msg.angular.z = 1.0
        self.pub.publish(msg)


def main():
    rclpy.init()
    node = Simple_pub()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("Keyboard stop")
        node.destroy_node()


if __name__ == "__main__":
    main()
