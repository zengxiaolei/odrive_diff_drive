from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    arg_show_rviz = DeclareLaunchArgument(
        "start_rviz",
        default_value="true",
        description="start RViz automatically with the launch file",
    )

    # Get URDF via xacro
    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            PathJoinSubstitution(
                [FindPackageShare("odrive_diff_drive"), "urdf",
                 "diffbot_system.urdf.xacro"]
            ),
        ]
    )
    robot_description = {"robot_description": robot_description_content}

    node_robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[robot_description],
    )

    odrive_diff_drive_controller = PathJoinSubstitution(
        [
            FindPackageShare("odrive_diff_drive"),
            "config",
            "odrive_diff_drive_controller.yaml",
        ]
    )

    controller_manager_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[robot_description, odrive_diff_drive_controller],
        output={
            "stdout": "screen",
            "stderr": "screen",
        },
    )

    dd_controller_spawner = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["odrive_diff_drive_controller",
                   "-c", "/controller_manager"],
        output="screen",
    )
    jsb_controller_spawner = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["joint_state_broadcaster", "-c", "/controller_manager"],
        output="screen",
    )

    rqt_publisher_node = Node(
        package="rqt_publisher",
        executable="rqt_publisher",
    )

    rviz_config_file = PathJoinSubstitution(
        [FindPackageShare("odrive_diff_drive"), "config", "odrive_rviz2.rviz"]
    )
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        arguments=["-d", rviz_config_file],
        condition=IfCondition(LaunchConfiguration("start_rviz")),
    )

    return LaunchDescription(
        [
            arg_show_rviz,
            node_robot_state_publisher,
            controller_manager_node,
            dd_controller_spawner,
            jsb_controller_spawner,
            rqt_publisher_node,
            rviz_node,
        ]
    )
