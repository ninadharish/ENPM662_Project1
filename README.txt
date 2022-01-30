# PROJECT-1 ENPM662
## Project Description
Simulation of the mini robot in Gazebo using ROS and control of the robot using teleop.

## Personnel

### Ameya Konkar

UID:118191058

### Ninad Harishchandrakar

UID:118150819

### Building the Program 

```
Please install ROS using the link: http://wiki.ros.org/Installation/Ubuntu
After installation follow the following commands,
mkdir -p ~/catkin_ws
cd ~/catkin_ws
catkin init
mkdir src
cd src
Paste the folder
cd ..
catkin_make clean && catkin_make
source ./devel/setup.bash
cd src/ mini_robot
Launch the robot: roslaunch mini_robot template_launch.launch
(open other terminal)
cd src/
chmod +x teleop_template.py 
Run the program teleop: rosrun mini_robot teleop_template.py 

```