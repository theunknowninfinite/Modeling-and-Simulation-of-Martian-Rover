# Mars-Rover

## Open Projects 2021   

## Abstract
<p align="justify">
 The <b>Mars Rover</b> is a small vehicle built to cover mars like uneven terrains. It is made to cover ueneven surfaces with ease and further to collect and analyze data. It has a robotic arm for data collection process and contains various sensors to recieve and record the data. It also has cameras, lidar and various other sensors for visual data interpretation and navigation.
</p>

<p align="center">
<img src="Images%20and%20Videos/Images/BEST%20RENDER!.jpg" alt="Mars Rover">
 <i>Mars Rover</i>
</p>

## Motivation
The Mars rover project helps us to learn the mechanisms and functioning of an actual rover sent to Mars under various space programmes. 

<p align="justify">
 It gives us an insight on the <b>Rocker Bogie</b> suspension system which facilitates the best possible movement of the Rover on challenging terrains. It also compelled us to think about a mechainism for a compact and fully functioning robotic arm which would be used to collect sample data.
</p>

<p align="justify">
The project also sheds light on the various sensors used by the rover for data collection and analysis as well as for its navigation. <b>Lidar</b> and <b>PIXL</b> are the senosrs used by us in the rover. 
</p>

The project also helped us learn detailed CAD modelling using Solidworks.

## Mechanical aspects of design
 
### Chassis
<p align="justify">
The main body of the rover is built up using 20*20 sq.mm aluminium T slots as frames. It consists of a top and a bottom frame (each of 382 * 283 mm T slots) connected using a metal connector where the rocker bogie would be attached. Each rectangular frame is made up using 2 different pipes of length 382mm and 283 mm along with 2 extra 283mm pipes attached in between the frame to give it extra stability and support. It is then covered with ABS plastic covers which are attached to the frame using bolts and nuts.
</p>

<p align="center">  
<img src="Images%20and%20Videos/Images/Chassis%20Mainframe.png" alt="Chassis">    
<i>Chassis</i>    
</p>  

### Rocker Bogie  
<p align="justify">
The Rocker Bogie is a six wheeled special suspension system used by the rover to ensure efficient motion on uneven terrains. It helps the mars rovers to overcome the rough terrains while maintaining stability by ensuring that all the wheel remain in contact with the ground. Each side of the suspension system is made up using 4 pipes of lengths 200, 170, 140 and 122mm(each of 314mm^2) which are connected using 3D printed connectors that facilitate the required motion of the suspension system. Both sides of the syspension are connected with the help of a differential bar placed on main frame of the rover. The middle of the bar is connected to the body with a pivot and the two ends are connected to the two rockers through some short links. If you hold the model rover body steady in midair and tilt one rocker up, one end of the bar will go back, the other end will go forward, and the other rocker will tilt down, thus maitaining the balance of the rover. 
</p>

<p align="center">
<img src="Images%20and%20Videos/Images/Rocker%20Bogie.png" alt="Rocker Bogie">
 <i>Rocker Bogie</i>
</p>

### Robotic Arm
The robotic arm is equipped with three modules: a drill, a camera and a sample collector, installed on a rotating disc.

It has 4 degrees of freedom(DOFs) as follows:  
1.The base can be rotated 360 degrees.  
2.The rotational joint can be rotated 180 degrees (range is limited by the counterweight)  
3.The main link contains a hydraulic/pneumatic cylinder which is used to extend/shorten the length of the link. The length of the link has a range of 33-43 cm.   
4.The rotating disc is used to engage either the drill or the sample collector with the Martian surface at a time.  

Thus, in a way, we have a handle on the three polar coordinates:
1. The base varies the planar angle 'theta'
2. The rotational joint varies the vertical angle 'phi'
3. Hydraulic/pneumatic cylinder varies radial distance 'r'
This makes inverse kinematics relatively simpler.
 
<p align="justify">
The camera is used all the time for navigation of the arm as well as scanning of the martian surface
Servo motors are used for precise actuation.
An air compressor/pump embedded in the rover body is used to create the necessary pressure differential to operate the pneumatic/hydraulic cylinder.
</p>

<p align="center">
<img src="Images%20and%20Videos/Images/Robotic%20Arm.JPG" alt="Robotic Arm">  
<i>Robotic Arm</i>
</p>
                                                                                                                                                 
### Wheels
The wheel can be 3D by more flexible materials like thermoplastic elastomers which has high impact strength and


### Mast Cam
<p align="justify">
The bottom part of the mast contains the stepper motor which is fixed to the body. A shaft extends to the upper part of the mast which can rotate horizontally and lies on a cylindrical thrust bearing. The camera is attached to the mast with the servo motor for vertical rotation.
</p>

<p align="center">
<img src="Images%20and%20Videos/Images/Mast%20cam.png" alt="Mast Cam")
<i>Mast Cam</i>
</p>

## CAD PARTS:
**IN CASE OF DISCREPANCY IN DOWNLOADING THE PARTS, KINDLY CHECK THE GIVEN DRIVE LINK:** https://drive.google.com/drive/folders/1dSjtfLlo9qPeHwJP8TGqEmEa5Fyg8wRc?usp=sharing


## Electronics aspects of design

### Sensors
1. **LIDAR sensor:**
<p align="justify">
Lidar is an acronym for “light detection and ranging.” It is sometimes called “laser scanning” or “3D scanning.” The technology uses eye-safe laser beams to create a 3D representation of the surveyed environment. This helps in navigation as well as analyzing the surrounding terrains and thus aids in the research part of the rover mission.
</p>

<p align="center">
<img src="Images%20and%20Videos/Images/LIDAR%20sensor.png" alt="LIDAR Sensor">
 <i> LIDAR Sensor</i>
</p>

2. **Mast Cam:**
<p align="justify">
The Mast Cam mounted over the chassis is used to get high definition videos and 3D-images of the surroundings which can be used for research purposes. It also has high zoom focus which can help in detailed examination of distant objects.
 </p>

3. **Robotic arm camera:**
<p align="justify">
A small camera is mounted on of the three modules of the robotic arm to assist in its motion and guide the drill to the required position. This makes teh collection of data sample more precise and accurate.
</p>

### Actuators
1. **DC motors:**
<p align="justify">
Six 12V DC motors with 20 RPM output are to be attached to the wheels which causes the locomotion of the Rover. The are placed in a holder attached to the Rocker Bogie and transmit torque to the wheels with the help of a small 3D printed shaft joining both these parts.
</p>

2. **Servo Motor:**
<p align="justify">
Four digital servo motors with 25kg cm torque output and operating voltage of 4.8-6.8 volts are used for steering the rover. The are attached to the rocker bogie with the help of a 3D printed holder connected on top of the dc motor holder. It enables the turning of front and rear pair of wheels and thus helps in turning the rover.
</p>

3. **Stepper motor:**
<p align="justify">
A 45kg-cm torque stepper motor is used for the horizontal rotation of the mast cam. The shaft of the stepper motor is attached to a threaded rod with a shaft coupler which transfers the rotation to the top part of the mast.
</p>

## Research part
<p align="justify">
We did an extensive research on the previously sent Mars Rovers and extracted details about the different components of the rover. We looked upon the structure and functioning of the parts and decided accordingly what to put in our rover. Although it was not practical to use all senosors and parts used by high end mars missions, we added whatever was possible in our reach to aid the research work of the rover.  
</p>

**This is the link of our initial research doc:** https://docs.google.com/document/d/1-jrgd7fFMnukzN-lmV8PeAjKU0p7QLTJImEPwY9DrF8/edit

## Cost Structure

| Components | Cost (in INR) |
|:----------------------------------:|:------------:|
| ABS plastic for 3d printing  | 16000 |
| T-slot Aluminium Extrussion | 360 |
| Battery  | 4300|
| Camera| 1500 |
| Stepper motors  | 725 |
| DC motors  | 3800 |
| Servo motors| 11250 |
| Servo horns | 375 |
| End joints | 800 |
| Nut and Bolts | 700 |
| Bearings | 900 |
| Lidar | 4850  |
| 4 thrust roller bearings| 3800 |
| Double acting mini pneumatic cylinder | 1258 |
| Single piston air compressor | 1000|
| Pneumatic tubing| 950 |
| Drill | 850 |
| Dc motor for drill: 15volt 11 watt | 3900 |
| Base servo motor 12volt  | 4950  |
| Joint servo motor 12volt |4950|
| Disc servo motor 12volt 2.9 watt| 3950 |
| Camera | 1250 |
| Sampler mechanism 5volt servo motor | 250 |
| Miscellaneous | 1500 |
|Total Cost| 74168 |

## Applications
1. The rover can be used to research the areas with highly uneven terrains and surfaces with ease due to its Rocker bogie suspension system.
2. It is equipped with a robotic arm and drill which enables sample data collection and storage.
3. The rover consists of a camera to take 3D images and high definition videos for mapping the terrain as well as analyzing it scientifically.
4. It can also be used to analyze the collected samples using the various sensors present on the rover

## Limitations
1. Speed of the rover is very low even on the flat terrains.
2. Battery life of the rover is short due to less charging capacity.

## Future Improvement
1. Better materials could be used instead of 3D printed plastic.  
2. Simulating the model in Gazebo and ROS.  


## Team members (with GitHub IDs)
1. <a href="https://github.com/matbot1">Avinash Singh</a>
2. <a href="https://github.com/MurkeyCube">Harikrishnan PB</a>
3. <a href="https://github.com/Pratyush-932">Pratyush Ojha</a>
4. <a href="https://github.com/SambitPrabhu">Sambit Prabhu</a>

## Mentors:
1.<a href="https://github.com/vanshgoyal">Vansh Goyal</a>

## Reference links
**Youtube-**  
<a href="https://www.youtube.com/watch?v=NOZZMsMAGh0&t=142s"> How I build mars rover replica </a>   
<a href="https://www.youtube.com/watch?v=McydwwR8xu4">[Mars Rover 2020 Perseverance] Body Assembly</a>  
<a href="https://www.youtube.com/watch?v=007SnaUxi40">JPL Mars Science Laboratory The Curiosity Rover</a>   


**Research links-**  
<a href="https://www.hindawi.com/journals/ijae/2016/5181097/"> Rocker Bogie Research </a>   
<a href="https://mars.nasa.gov/mars2020/spacecraft/rover/"> NASA Mars Rover (Perseverance) </a>   
<a href="https://llis.nasa.gov/lesson/11501">Actuator Design process for curiosity</a>     
<a href="http://robotics.estec.esa.int/ASTRA/Astra2004/Papers/astra2004_D-05.pdf">Types of Rocker Bogies</a>  
<a href="https://teamares.sserd.org/project_files/Ares_MCEV_Report.pdf"> Research paper for design of crew exploration vehicle on Mars</a>  


