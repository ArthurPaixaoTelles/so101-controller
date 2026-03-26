import mujoco
import mujoco.viewer
import threading
import numpy as np
import time
import os

JOINT_INDEX = {
    "shoulder_pan":  0,
    "shoulder_lift": 1,
    "elbow_flex":    2,
    "wrist_flex":    3,
    "wrist_roll":    4,
    "gripper":       5,
}

class Simulation:
    def __init__(self):
        xml_path = os.getenv("MUJOCO_XML_PATH", "/home/aptm/lerobot/SO-ARM100/Simulation/SO101/scene.xml")
        self.m = mujoco.MjModel.from_xml_path(xml_path)
        self.d = mujoco.MjData(self.m)
        if os.getenv("MUJOCO_VIEWER", "false") == "true":
            thread = threading.Thread(target=self._launch_viewer)
            thread.daemon = True
            thread.start()

    def _launch_viewer(self):
        with mujoco.viewer.launch_passive(self.m, self.d) as v:
            while v.is_running():
                v.sync()
                time.sleep(0.01)

    def update_joints(self, joints_in_rad: dict):
        print("simulation recebeu:", joints_in_rad)  # ← adiciona isso
        for name, value in joints_in_rad.items():
            indice = JOINT_INDEX[name]
            min_val = self.m.jnt_range[indice][0]
            max_val = self.m.jnt_range[indice][1]
            self.d.qpos[indice] = float(np.clip(value, min_val, max_val))
        mujoco.mj_forward(self.m, self.d)
        print("qpos após update:", self.d.qpos[:6])  # ← e isso