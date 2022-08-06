odrive_diff_drive ROS2 Package
=============================

The odrive_diff_drive package implements a use case of diff_drive_controller based on ODrive driver for ros2_control. It provides a clear and simple template for faster implementation of custom hardware and controllers.

### Requirements
Make sure that the following packages and their depends are installed.
- [odrive_ros2_control](https://github.com/Factor-Robotics/odrive_ros2_control/wiki/Documentation)
- [ros2_control](https://github.com/ros-controls/ros2_control)

### Prerequisites
* ROS Foxy (Tested)
* Power Supply
* ODrive with two pairs of motors and encoders connected

### Usage
You can modify the controller parameters if needed or leave them unchanged. Launch all function by the following command.
```
ros2 launch odrive_diff_drive odrive_diff_drive.launch.py
```
You can modify and send velocity commands by rqt_publisher UI.

<img src="https://github.com/zengxiaolei/robotics_demo/blob/master/drive/odrive_diff_drive/rqt_publisher.png" width="500">

If all goes well, the motors run according to your velocity command, you can also see the coordinate system movement in RVIZ.


### Videos
Note, the two videos are not synchronized.


https://user-images.githubusercontent.com/34747839/183235842-862c43dc-9eea-4ba9-9407-73d0bb66feca.mp4




https://user-images.githubusercontent.com/34747839/183235847-ab0242e1-4994-43de-b18d-f70fedd95f21.mp4


### reference
- [ODrive Documentation](https://docs.odriverobotics.com/v/0.5.4/index.html)
- [ros2_control Demos](https://github.com/ros-controls/ros2_control_demos)
