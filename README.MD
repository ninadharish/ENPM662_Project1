# Mini Car Simulation Using ROS

## Description

A mini car is modeled in SolidWorks and simulated in Gazebo using the Robot Operating System (ROS). This mini car is controlled using keyboard inputs using a Teleop node.

## Output

The car travels with the help of the teleop keyboard inputs in the Gazebo Simulation. The LIDAR sensor input can be seen on the RViz tab.

![alt text](/output/mini_car_teleop.png)

The Video Output can be found [here](https://drive.google.com/file/d/1TRkTmKLdPHWGQYnXYA0QviBPUNWJVha1/view?usp=sharing).


## Getting Started

### Dependencies

<p align="left"> 
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>&ensp; </a>
<a href="https://www.ros.org/" target="_blank" rel="noreferrer"> <img align="bottom" src="https://upload.wikimedia.org/wikipedia/commons/b/bb/Ros_logo.svg" alt="ROS" width="70" height="40"/> &ensp;</a>
<a href="https://gazebosim.org/" target="_blank" rel="noreferrer"> <img align="bottom" src="https://upload.wikimedia.org/wikipedia/en/thumb/5/5e/Gazebo_logo_without_text.svg/300px-Gazebo_logo_without_text.svg.png?20150715002113" alt="Gazebo" width="60" height="50"/>&ensp; </a>
<a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> &ensp;</a>

* [Python 3](https://www.python.org/)
* [Robot Operation System (ROS)](http://wiki.ros.org/)

### Installing

* Install ROS using the instructions on the [link](http://wiki.ros.org/Installation/Ubuntu).

### Executing program

After ROS installation, follow the instructions to execute the program:

* Create and build the Catkin Workspace.
```
mkdir -p ~/catkin_ws
cd ~/catkin_ws
catkin init
mkdir src
catkin build
source ./devel/setup.bash
cd src
mkdir mini_car_teleop
cd mini_car_teleop
```
* Paste the contents of the package into the 'mini_car_teleop' folder and build the Catkin Workspace again.
```
cd ..
cd ..
catkin build
source ./devel/setup.bash
```
* Launch the Gazebo Simulation
```
roslaunch mini_car_teleop template_launch.launch
```
* Run the Teleop node to control the car using keyboard inputs by following the instructions on the screen.
```
rosrun mini_robot teleop_template.py 
```

## Authors

👤 **Ninad Harishchandrakar**

* [GitHub](https://github.com/ninadharish)
* [Email](ninad.harish@gmail.com)
* [LinkedIn](https://linkedin.com/in/ninadharish)
