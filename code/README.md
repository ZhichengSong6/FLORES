# Quadruped ROS2 Control

This repository contains the ros2-control based controllers for the quadruped robot.

* [Controllers](Mdog/controllers): contains the ros2-control controllers
* [Commands](Mdog/commands): contains command node used to send command to the controller
* [Descriptions](Mdog/descriptions): contains the urdf model of the robot
* [Hardwares](Mdog/ardwares): contains the ros2-control hardware interface for the robot

# RL Controller
Tested environment:
* Ubuntu 22.04
    * ROS2 Humble

## Quick Start

### Installing libtorch

> You can also choose `libtorch` with cuda. Just remember to download for c++ 11 ABI version. The position to place `libtorch` is also not fixed, just need to config the `.bashrc`.

```bash
cd ~/CLionProjects/
wget https://download.pytorch.org/libtorch/cpu/libtorch-cxx11-abi-shared-with-deps-2.5.0%2Bcpu.zip
unzip libtorch-cxx11-abi-shared-with-deps-2.5.0+cpu.zip
```

```bash
cd ~
rm -rf libtorch-cxx11-abi-shared-with-deps-2.5.0+cpu.zip
echo 'export Torch_DIR=~/libtorch' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/libtorch/lib' >> ~/.bashrc
```

### Installing ros2_control
```bash
sudo apt install ros-humble-ros2-control
sudo apt install ros-humble-ros2-controllers
```

### Build the Controller
1. Put the `Mdog` file in the `src` file in your ros2_ws.
2. Install dependency and compile the package
* rosdep
    ```bash
    cd ~/ros2_ws
    rosdep install --from-paths src --ignore-src -r -y
    ```
* Compile the package
    ```bash
    colcon build --packages-up-to rl_quadruped_controller mdog_description keyboard_input hardware_unitree_mujoco --symlink-install
    ```

### Install Mujuco
1. please refer to [unitree_mujoco](https://github.com/unitreerobotics/unitree_mujoco) for C++ version installation details.
2. Copy [mdog](xml/mdog) file to the `unitree_mujoco/unitree_robots` file.
3. Change to `robot:"mdog"` type in `unitree_mujoco/simulate/config.yaml`

### Start Simulation
1. Start Mujoco first.
   ```bash
   cd ~/{unitree_mujoco}/simulate/build
   ./unitree_mujoco
   ```
2. Open another terminal and launch the rl_controller
   ```bash
   cd ~/ros2_ws
   source install/setup.bash 
   ros2 launch rl_quadruped_controller mujoco.launch.py
   ```
3. Open another terminal and run the `keyboard_control` node
   ```bash
   cd ~/ros2_ws
   source install/setup.bash 
   ros2 run keyboard_input keyboard_input
   ```

### Instructions
#### 1.1 Control Mode
* Passive Mode: Keyboard 1
* Fixed Stand: Keyboard 2
    * RL mode: Keyboard 3
#### 1.2 Control Input
* WASD IJKL: Move robot
* Space: Reset Speed Input

## RL Policy and HIMLoco Training

We provide the trained HIM-based locomotion policy and the corresponding FLORES environment files for RL training.

### Pre-trained Policy

The pre-trained HIM-based policy checkpoint is available on Hugging Face:

[szc97/FLORES-HIMLoco-Policy](https://huggingface.co/szc97/FLORES-HIMLoco-Policy)

A local copy of the checkpoint is also available at:

```text
code/Mdog/descriptions/mdog/mdog_description/config/legged_gym/May22_0943.pt
```
This checkpoint is trained for the FLORES wheeled-quadrupedal robot using the HIMLoco-based reinforcement learning pipeline.

### Training Environment Files

The FLORES environment files for HIMLoco are provided in:
```text
code/HIM_FLORES/
```
These files include:
```text
mdog_config.py
mdog_robot.py
```
To use them, first install HIMLoco, then place the two files under:
```text
HIMLoco/legged_gym/legged_gym/envs/mdog/
```
The expected structure is:
```text
HIMLoco/
└── legged_gym/
    └── legged_gym/
        └── envs/
            └── mdog/
                ├── mdog_config.py
                └── mdog_robot.py
```
Please also place the FLORES URDF and mesh files under:
```text
HIMLoco/legged_gym/resources/robots/mdog/
```
Then register the environment in:
```text
HIMLoco/legged_gym/legged_gym/envs/__init__.py
```
by adding:
```code
from legged_gym.envs.mdog.mdog_config import MdogRoughCfg, MdogRoughCfgPPO
from legged_gym.envs.mdog.mdog_robot import mDog

task_registry.register("mdog", mDog, MdogRoughCfg(), MdogRoughCfgPPO())
```
After registration, train the policy with:
```bash
cd HIMLoco/legged_gym/legged_gym/scripts
python train.py --task=mdog
```
For more details, please refer to:
```text
code/HIM_FLORES/README.md
```
### Notes

- The provided policy is trained for the FLORES `mdog` model.
- The current environment uses 16 actions corresponding to the robot joints.
- If the robot model, observation structure, or terrain sensing setup is modified, the policy and environment configuration may need to be retrained or adjusted.