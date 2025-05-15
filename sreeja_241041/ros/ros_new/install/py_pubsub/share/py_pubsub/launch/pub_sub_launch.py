from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    custom_message = LaunchConfiguration('custom_message')

    return LaunchDescription([
        DeclareLaunchArgument(
            'custom_message',
            default_value='Hello AUV!',
            description='Message to publish from talker node'
        ),
        Node(
            package='py_pubsub',
            executable='talker',
            name='talker',
            parameters=[{'custom_message': ParameterValue(custom_message, value_type=str)}],
            output='screen'
        ),
        Node(
            package='py_pubsub',
            executable='listener',
            name='listener',
            output='screen'
        ),
    ])
