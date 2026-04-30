# SPDX-FileCopyrightText: Copyright (c) 2021 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Copyright (c) 2021 ETH Zurich, Nikita Rudin

from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO

class MdogRoughCfg( LeggedRobotCfg ):
    class env( LeggedRobotCfg.env):
        num_actions = 16
        num_envs = 4096
        num_one_step_observations = 57 
        num_observations = num_one_step_observations * 12
        num_one_step_privileged_obs = 57 + 3 + 3 + 187 # additional: base_lin_vel, external_forces, scan_dots 253
        num_privileged_obs = num_one_step_privileged_obs * 1

    class init_state( LeggedRobotCfg.init_state ):

        # # normal pose
        pos = [0.0, 0.0, 0.65] # x,y,z [m]
        default_joint_angles = { # = target angles [rad] when action = 0.0
            'FL_hip_joint': 0.00,   # [rad]
            'FL_thigh_joint': 0.8,   # [rad]
            'FL_calf_joint': -0.65,   # [rad]
            'FL_ankle_joint': 0.0 ,  # [rad]

            'FR_hip_joint': 0.00,   # [rad]
            'FR_thigh_joint': -0.8,  # [rad]
            'FR_calf_joint': 0.65,   # [rad]
            'FR_ankle_joint': 0.0,   # [rad]

            'RL_hip_joint': 0.0,   # [rad]
            'RL_thigh_joint': 0.85,   # [rad]
            'RL_calf_joint': -0.65,   # [rad]
            'RL_ankle_joint': 0.0,   # [rad]

            'RR_hip_joint': 0.0,   # [rad]
            'RR_thigh_joint': -0.85,   # [rad]
            'RR_calf_joint': 0.65,   # [rad]
            'RR_ankle_joint': 0.0,   # [rad]
        }


    class terrain( LeggedRobotCfg.terrain ):
        # mesh_type = 'plane'
        # mesh_type = 'heightfield'
        mesh_type = 'trimesh'
        # terrain types: [smooth slope, rough slope, stairs up, stairs down, discrete]
        # terrain_proportions = [0.1, 0.1, 0.5, 0.2, 0.1]
        # terrain_proportions = [0.0, 0.0, 1.0, 0.0, 0.0]
        # measure_heights = False

    class control( LeggedRobotCfg.control ):
        # PD Drive parameters:
        control_type = 'P'
        # stiffness = {'joint': 500.0}  # [N*m/rad]
        # damping = {'joint': 10.0}     # [N*m*s/rad]
        stiffness = {'FL_hip_joint': 35.,'FL_thigh_joint': 35.,'FL_calf_joint': 35.,"FL_ankle_joint":0,
                     'FR_hip_joint': 35.,'FR_thigh_joint': 35.,'FR_calf_joint': 35.,"FR_ankle_joint":0,
                     'RL_hip_joint': 35.,'RL_thigh_joint': 35.,'RL_calf_joint': 35.,"RL_ankle_joint":0,
                     'RR_hip_joint': 35.,'RR_thigh_joint': 35.,'RR_calf_joint': 35.,"RR_ankle_joint":0}  # [N*m/rad]
        damping =   {'FL_hip_joint': 2.0,'FL_thigh_joint':  2.0,'FL_calf_joint':  2.0,"FL_ankle_joint": 3,
                     'FR_hip_joint': 2.0,'FR_thigh_joint':  2.0,'FR_calf_joint':  2.0,"FR_ankle_joint": 3,
                     'RL_hip_joint': 2.0,'RL_thigh_joint':  2.0,'RL_calf_joint':  2.0,"RL_ankle_joint": 3,
                     'RR_hip_joint': 2.0,'RR_thigh_joint':  2.0,'RR_calf_joint':  2.0,"RR_ankle_joint": 3}  # [N*m*s/rad]
        # stiffness = {'hip_joint': 200.,'thigh_joint': 300.,'calf_joint': 300.,"ankle_joint":75}  # [N*m/rad]
        # damping = {'hip_joint': 5,'thigh_joint': 5,'calf_joint': 2,"ankle_joint":0.5}     # [N*m*s/rad]
        # action scale: target angle = actionScale * action + defaultAngle
        action_scale = 0.25
        # decimation: Number of control action updates @ sim DT per policy DT
        decimation = 4
        hip_reduction = 1.0
        wheel_reduction = 1.0 # all other joints reduction is 10, the wheel joints are 10

    class commands( LeggedRobotCfg.commands ):
            curriculum = True
            max_curriculum = 2.0
            num_commands = 4 # default: lin_vel_x, lin_vel_y, ang_vel_yaw, heading (in heading mode ang_vel_yaw is recomputed from heading error)
            resampling_time = 10. # time before command are changed[s]
            heading_command = True # if true: compute ang vel command from heading error
            class ranges( LeggedRobotCfg.commands.ranges):
                lin_vel_x = [-2.0, 2.0] # min max [m/s]
                # lin_vel_x = [-0.0, 0.0] # min max [m/s]
                lin_vel_y = [-1.5, 1.5]   # min max [m/s]
                # lin_vel_y = [-0.0, 0.0]   # min max [m/s]
                ang_vel_yaw = [-3.14, 3.14]    # min max [rad/s]
                # ang_vel_yaw = [-0.0, 0.0]    # min max [rad/s]
                heading = [-3.14, 3.14]

    class asset( LeggedRobotCfg.asset ):
        file = '{LEGGED_GYM_ROOT_DIR}/resources/robots/mdog/urdf/mdog.urdf'
        # file = '{LEGGED_GYM_ROOT_DIR}/resources/robots/mdog_stand/urdf/robot4.urdf'
        # file = '{LEGGED_GYM_ROOT_DIR}/resources/robots/mdog_pos2/urdf/robot4_pos2.urdf'
        name = "mdog"
        foot_name = "wheel"
        wheel_joint_name =[ "ankle_joint"] #wheel joints name, joint name
        leg_joint_name = ["FR","FL","RR","RL"] #leg joints name, joint name
        penalize_contacts_on = [ "calf", "thigh"] # TODO
        terminate_after_contacts_on = ["base", "hip", "thigh"] # TODO
        privileged_contacts_on = ["base", "thigh", "calf"] # TODO
        self_collisions = 1 # 1 to disable, 0 to enable...bitwise filter
        flip_visual_attachments = False # Some .obj meshes must be flipped from y-up to z-up
  
    class rewards( LeggedRobotCfg.rewards ):
        class scales:
            termination = -0.0
            tracking_lin_vel = 8.0
            tracking_ang_vel = 4.0
            lin_vel_z = -0.1
            ang_vel_xy = -0.05

            orientation = -1.0
            base_height = 2.0
            stand_still = 5.0
            dof_error = 1.0

            dof_acc = -2.5e-7
            joint_power = -5e-5
            torques = -5e-5
            action_rate = -0.01
            smoothness = -0.01

            dof_pos_limits = -0.05
            dof_vel_limits = -0.0
            torque_limits = -0.1

            feet_contact_forces = -0.05
            stand_still_rear_hip = 1.0


        only_positive_rewards = True # if true negative total rewards are clipped at zero (avoids early termination problems)
        tracking_sigma = 0.25 # tracking reward = exp(-error^2/sigma)
        base_height_sigma = 1.0
        standstill_sigma = 0.25

        nominal_foot_position_tracking_sigma = 0.005
        nominal_foot_position_tracking_sigma_wrt_v = 0.5

        soft_dof_pos_limit = 0.9 # percentage of urdf limits, values above this limit are penalized
        soft_dof_vel_limit = 1.
        soft_torque_limit = 0.9
        base_height_target = 0.6
        foot_radius = 0.125
        max_contact_force = 250. # forces above this value are penalized
        clearance_height_target = -0.325 + foot_radius

    class normalization( LeggedRobotCfg.normalization ):
        class obs_scales( LeggedRobotCfg.normalization.obs_scales ):
            lin_vel = 2.0
            ang_vel = 0.25
            dof_pos = 1.0
            dof_vel = 0.05
            height_measurements = 5.0
        clip_observations = 100.
        clip_actions = 100.

class MdogRoughCfgPPO(LeggedRobotCfgPPO):
    class algorithm( LeggedRobotCfgPPO.algorithm ):
        entropy_coef = 0.005
    class runner( LeggedRobotCfgPPO.runner ):
        run_name = ''
        experiment_name = 'rough_mdog'
        max_iterations = 10000 # number of policy updates
        # logging
        save_interval = 1000 # check for potential saves every this many iterations

        resume = False
        # resume = True
        # resume_path = ''

  