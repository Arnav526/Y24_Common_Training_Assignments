from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'message',
            default_value='Custom launch message!',
            description='Message to publish'
        ),
        Node(
            package='talker_listener',
            executable='talker',
            name='talker',
            parameters=[{'message': LaunchConfiguration('message')}]
        ),
        Node(
            package='talker_listener',
            executable='listener',
            name='listener'
        )
    ])
