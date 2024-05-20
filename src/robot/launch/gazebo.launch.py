import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    package_name = 'robot'
    pkg_share = get_package_share_directory(package_name)

    urdf_file = os.path.join(pkg_share, 'urdf', 'robot.urdf')
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    rviz_config_file = os.path.join(pkg_share, 'configs', 'robot_config.rviz')

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation (Gazebo) clock if true'),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'four_wheel_robot', '-file', urdf_file],
            output='screen'),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_file],
            parameters=[{'use_sim_time': use_sim_time}]),

        Node(
            package=package_name,
            executable='move_circle',
            name='move_circle',
            output='screen',
        ),
    ])

