from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():

    config = os.path.join(
        get_package_share_directory('lqr_ros2_node_project'),
        'config',
        'params.yaml'
        )
    
    return LaunchDescription([
        Node(
            package="lqr_ros2_node_project",
            executable="lqr_node",
            parameters = [config],
            name="lqr_node",
            output="screen",
        )
    ])
