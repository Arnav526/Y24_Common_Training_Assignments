# launch/talk_listen.launch.py
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'message',
            default_value='Hello from launch!',
            description='Message to publish'
        ),
        Node(
            package='my_talker_listener',
            executable='talker',
            name='talker',
            parameters=[{'message': LaunchConfiguration('message')}]
        ),
        Node(
            package='my_talker_listener',
            executable='listener',
            name='listener'
        )
    ])
