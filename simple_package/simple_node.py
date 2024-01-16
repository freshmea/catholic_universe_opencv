import rclpy
from rclpy.node import Node


def print_hellow():
    print("first node")
    print("hellow")


def main():
    rclpy.init()
    node = Node("simple_node")  # type: ignore
    node.create_timer(1, print_hellow)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("Keyboard stop")
        node.destroy_node()


if __name__ == "__main__":
    main()
