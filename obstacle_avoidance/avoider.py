import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class Avoider(Node):

    def __init__(self):
        super().__init__('avoider')

        self.sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.callback,
            10
        )

        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)

    def callback(self, msg):
        cmd = Twist()

        front = min(min(msg.ranges[0:15]), min(msg.ranges[-15:]))

        if front < 0.7:
            cmd.linear.x = 0.0
            cmd.angular.z = 0.8
        else:
            cmd.linear.x = 0.25
            cmd.angular.z = 0.0

        self.pub.publish(cmd)


def main():
    rclpy.init()
    node = Avoider()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
