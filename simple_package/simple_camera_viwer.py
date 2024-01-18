import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
import cv2
from cv_bridge import CvBridge, CvBridgeError
import numpy as np


class Simple_camera_viewer(Node):
    def __init__(self):
        super().__init__("simple_camera_viewer")  # type: ignore
        self.create_subscription(
            CompressedImage, "/image_raw/compressed", self.sub_image, 10
        )
        self.cv = CvBridge()

    def sub_image(self, msg: CompressedImage):
        frame = np.zeros((480, 640, 3), np.uint8)
        try:
            frame = self.cv.compressed_imgmsg_to_cv2(msg, "bgr8")
        except CvBridgeError as e:
            self.get_logger().info(e)
        cv2.imshow("image", frame)
        cv2.waitKey(1)


def main():
    rclpy.init()
    node = Simple_camera_viewer()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("Keyboard stop")
        node.destroy_node()


if __name__ == "__main__":
    main()
