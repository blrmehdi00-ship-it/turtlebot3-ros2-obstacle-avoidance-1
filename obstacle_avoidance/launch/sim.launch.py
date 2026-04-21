from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os


def generate_launch_description():

    os.environ['TURTLEBOT3_MODEL'] = 'burger'

    return LaunchDescription([

        # Gazebo simulation
        ExecuteProcess(
            cmd=['gz', 'sim', '-r'],
            output='screen'
        ),

        # TurtleBot3 simulation (package officiel)
        ExecuteProcess(
            cmd=[
                'ros2', 'launch',
                'turtlebot3_gazebo',
                'turtlebot3_world.launch.py'
            ],
            output='screen'
        ),

        # Ton node
        Node(
            package='turtlebot3_obstacle_avoidance',
            executable='avoider',
            output='screen'
        )
    ])
