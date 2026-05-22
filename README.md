# A Reconfigured Wheel-Legged Robot for Enhanced Steering and Adaptability

<p align="center">
  <a href="https://ieeexplore.ieee.org/document/11495517">
    <img src="https://img.shields.io/badge/IEEE%20RA--L-2026-blue">
  </a>
</p>

<p align="center">
  <strong>Published in IEEE Robotics and Automation Letters (RA-L), 2026.</strong><br>
  Please cite the peer-reviewed RA-L version if this project is useful for your research.
</p>
<p align ="center">
<img src="fig/dof_property.jpg" width=75%>
</p>

Overview of mechanical design: (a) Illustration of the joint DoF design for FLORES, along with the positioning of electrical components. The magnified view on the lower side shows the joint layout of the front left leg. (b) Range of motion for the front hip joint. (c) Range of motion for the rear hip joint.

<p align ="center">
<img src="fig/system_framework.png" width=90%>
</p>

Overview of our system architecture and training pipeline. The training process consists of two phases: Phase I involves sim-to-sim transfer, where the HIM policy is first trained in Isaac Gym with reward shaping, and then is transferred and validated in MuJoCo as an intermediate step; Phase II performs Sim2Real deployment using ROS2 control framework to establish robot communications. The hardware framework (right panel) shows the onboard PC receiving user input and combining it with current observations to feed into the trained RL model, which outputs actions for robot control. Red lines indicate power connections, and black arrows show the information flow.

## Results

### FLORES Navigating on Various Terrains
<p align ="center">
<img src="fig/terrain1_2x.gif" width=75%>
</p>

<p align ="center">
<img src="fig/terrain2_2x.gif" width=75%>
</p>

<p align ="center">
<img src="fig/stairs.gif" width=75%>
</p>

### FLORES and B2W Perform Lateral Walking
<p align ="center">
<img src="fig/Lateral_Ours.gif" width=75%>
</p>

<p align ="center">
<img src="fig/Lateral_B2W.gif" width=75%>
</p>

### FLORES and B2W Perform Stright-line Motion

command speed = 0.5 m/s
<p align ="center">
<img src="fig/Discrete_0.5_2x.gif" width=75%>
</p>
<p align ="center">
<img src="fig/Grassland_0.5_2x.gif" width=75%>
</p>
<p align ="center">
<img src="fig/Gravels_0.5_2x.gif" width=75%>
</p>
<p align ="center">
<img src="fig/PavedGround_0.5_2x.gif" width=75%>
</p>
command speed = 1.0 m/s
<p align ="center">
<img src="fig/Discrete_1.0.gif" width=75%>
</p>
<p align ="center">
<img src="fig/Grassland_1.0.gif" width=75%>
</p>
<p align ="center">
<img src="fig/Gravels_1.0.gif" width=75%>
</p>
<p align ="center">
<img src="fig/PavedGround_1.0.gif" width=75%>
</p>

command speed = 1.5 m/s
<p align ="center">
<img src="fig/Discrete_1.5.gif" width=75%>
</p>
<p align ="center">
<img src="fig/Grassland_1.5.gif" width=75%>
</p>
<p align ="center">
<img src="fig/Gravels_1.5.gif" width=75%>
</p>
<p align ="center">
<img src="fig/PavedGround_1.5.gif" width=75%>
</p>

### FLORES and B2W Perform Turning Maneuver
radius = 0.5m
<p align ="center">
<img src="fig/Turning_0.5.gif" width=75%>
</p>
radius = 1.0m
<p align ="center">
<img src="fig/Turning_1.0.gif" width=75%>
</p>
radius = 1.5m
<p align ="center">
<img src="fig/Turning_1.5.gif" width=75%>
</p>
radius = 2.0m
<p align ="center">
<img src="fig/Turning_2.0.gif" width=75%>
</p>

### FLORES and B2W Perform Path Tracking
<p align ="center">
<img src="fig/PathFollowing_Ours.gif" width=75%>
</p>
<p align ="center">
<img src="fig/PathFollowing_B2W.gif" width=75%>
</p>

### FLORES and B2W Performance under Difference Disturbance in Simulation
<p align ="center">
<img src="fig/disturbance.gif" width=75%>
</p>

### Front Legs' Joint Velocity of FLORES when Traversing Obstacles in Simulation
<p align ="center">
<img src="fig/left_right_stairs.gif" width=75%>
</p>

## Mechanical Parts
All machined parts are manufactured with outsourced CNC service. The .stl file of all the parts can be found in Mechanical floder.

## Hardware Device
All hardware device installed in FLORES can be found in the table below.
<p align ="center">
<img src="fig/Hardware_Device_List.png" width=75%>
</p>

## Authors


