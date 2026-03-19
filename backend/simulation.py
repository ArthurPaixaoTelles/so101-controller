import mujoco
import mujoco.viewer
import threading
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
        self.viewer = None
        if os.getenv("MUJOCO_VIEWER", "false") == "true":
            thread = threading.Thread(target=self._launch_viewer)
            thread.daemon = True
            thread.start()
    def _launch_viewer(self):
        mujoco.viewer.launch(self.m, self.d)
    def update_joints(self, joints_in_rad: dict):
        for name, value in joints_in_rad.items():
            indice = JOINT_INDEX[name]  
            self.d.qpos[indice] = value 
            mujoco.mj_step(self.m, self.d)  