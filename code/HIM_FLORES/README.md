# FLORES HIMLoco Training Files

This folder provides the FLORES environment files for HIM-based locomotion training with [HIMLoco](https://github.com/InternRobotics/HIMLoco).

## Files

- `mdog_config.py`: environment and PPO configuration for FLORES.
- `mdog_robot.py`: FLORES robot environment implementation for HIMLoco / `legged_gym`.

## Where to Place These Files

After installing HIMLoco, create the following folder inside the HIMLoco repository:

```bash
mkdir -p HIMLoco/legged_gym/legged_gym/envs/mdog
```

Then copy the two files into this folder:
```bash
cp mdog_config.py HIMLoco/legged_gym/legged_gym/envs/mdog/
cp mdog_robot.py HIMLoco/legged_gym/legged_gym/envs/mdog/
```
The final structure should be:
```text
HIMLoco/
└── legged_gym/
    └── legged_gym/
        └── envs/
            └── mdog/
                ├── mdog_config.py
                └── mdog_robot.py
```

## Robot Asset Path

The default robot asset path in mdog_config.py is:
```text
file = '{LEGGED_GYM_ROOT_DIR}/resources/robots/mdog/urdf/mdog.urdf'
```
Therefore, please place the FLORES URDF and mesh files under:
```text
HIMLoco/legged_gym/resources/robots/mdog/
```
The expected URDF path is:
```text
HIMLoco/legged_gym/resources/robots/mdog/urdf/mdog.urdf
```
If your robot asset is placed elsewhere, please modify the file field in mdog_config.py.

## Register the Environment

After copying the files, register the FLORES environment in:
```text
HIMLoco/legged_gym/legged_gym/envs/__init__.py
```
Add the following lines:
```code
from legged_gym.envs.mdog.mdog_config import MdogRoughCfg, MdogRoughCfgPPO
from legged_gym.envs.mdog.mdog_robot import mDog

task_registry.register("mdog", mDog, MdogRoughCfg(), MdogRoughCfgPPO())
```
## Training

After registration, train the policy from the HIMLoco script directory:
```bash
cd HIMLoco/legged_gym/legged_gym/scripts
python train.py --task=mdog
```
## Notes
These files are intended to be used together with the original HIMLoco codebase.
Please follow the [HIMLoco installation instructions](https://github.com/InternRobotics/HIMLoco) first, including Isaac Gym, `rsl_rl`, and `legged_gym` setup.
The current configuration uses 16 actions and the FLORES mdog URDF.
If you modify the observation structure, terrain sensing, or robot model, please also update the observation dimensions in mdog_config.py.