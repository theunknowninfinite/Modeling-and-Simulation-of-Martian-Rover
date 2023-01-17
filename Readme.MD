# ENPM662 - Project 2  <br /> Modeling and Simulation of Martian Rover



## Authors

- [Suriya Suresh](https://www.github.com/theunknowninfinite)
- [Sandip Sharan Senthil Kumar](https://github.com/sandipsharan)

## 1. Project Goals

* Design a Martian Rover and a 5 DoF manipulator.
* Calculate and verify the kinematics of the manipulator.
* Simulate the rover in a Martian Environment.
* Control the rover in simulation.
* Execute the task of drilling into the surface in simulation.
* Integration of a camera onto the rover.
## 2. Installation of Dependencies
ROS is required to this package.
Install ROS by follwoing the instructions on:
http://wiki.ros.org/noetic/Installation

## 3. Setting up the package

1. Clone the github repo.

```` 
$ git clone link-of-repo
````

2. Inside the repo under package is the ROS package which is required to run the robot & the package is named as robo_car

3. Go to your catkin_ws by typing the command  ````$ cd <your catkin_ws_name>```` 

4. Place that package in your catkin_ws under src 

5. Then run the command ```` $ catkin_make clean && catkin_make ```` to build the package

6. Source everytime you open a new terminal or made any changes in the ROS package using the command
````
source devel/setup.bash
````
## 4. Visualizing output of Camera 

1. Open two terminals and source ROS using the command mentioned above <br />

2. Run the command below to launch the toy car in Gazebo environment
```` 
roslaunch mars_rover_v8 template_launch.launch 
```` 
3. In your other terminal run the command, to launch RViz
````
rosrun rviz rviz
````
4. Add the RobotModel and Camera. There you go you can see the Rover and Camera visualization in RViz

## 5. Instructions to run the Rover in Gazebo 

1. Open two terminals and source ROS using the command mentioned above <br />

2. Run the command below to launch the toy car in Gazebo environment
```` 
roslaunch mars_rover_v8 template_launch.launch 
```` 
3. In your other terminal run the command, to launch the teleop controllers
````
rosrun mars_rover_v8 Script_move.py
````

## Credits 
Credits to the repsective owners of trademarks and to 
* NASA for openly available models of their Mars rovers 
* [TheConstructCore](https://bitbucket.org/theconstructcore/curiosity_mars_rover/src/master/) for their Curiosity Mars Rover package from which the envrionment was used 
* https://github.com/marsiitr/Mars-Rover for their Model of the Mars Rover used for this project
* https://github.com/fath25/AachenRover for their model of the Mars Rover, the arm from it being used for this project 

