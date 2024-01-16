import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

MAX_LIN = 0.21
MAX_ANG = 2.84


class Simple_turtlemove(Node):
    def __init__(self):
        super().__init__("simple_turtlemove")  # type: ignore
        self.create_timer(0.1, self.pub_callback)
        self.pub = self.create_publisher(Twist, "/cmd_vel", 10)

    def pub_callback(self):
        msg = Twist()
        msg.linear.x = 0.1
        msg.angular.z = 1.0

        msg = self.restrain(msg)
        self.pub.publish(msg)

    def restrain(self, msg: Twist):
        if msg.linear.x > MAX_LIN:
            msg.linear.x = MAX_LIN
        elif msg.linear.x < -MAX_LIN:
            msg.linear.x = -MAX_LIN
        if msg.angular.z > MAX_ANG:
            msg.angular.z = MAX_ANG
        elif msg.angular.z < -MAX_ANG:
            msg.angular.z = -MAX_ANG
        return msg


def main():
    rclpy.init()
    node = Simple_turtlemove()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("Keyboard stop")
        node.destroy_node()


if __name__ == "__main__":
    main()
