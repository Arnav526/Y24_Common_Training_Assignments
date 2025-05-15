from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_assignment_pkg',
            executable='talker',
            name='talker',
            parameters=[{'talker_message': 'Hello from launch file!'}],
            output='screen'
        ),
        Node(
            package='ros2_assignment_pkg',
            executable='listener',
            name='listener',
            output='screen'
        ),
    ])
