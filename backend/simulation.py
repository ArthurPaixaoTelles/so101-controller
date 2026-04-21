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
        
        # O Lock é essencial para evitar o erro de "stack is in use"
        self._lock = threading.Lock()

        # Iniciar a Thread de Física
        self.physics_thread = threading.Thread(target=self._physics_loop)
        self.physics_thread.daemon = True
        self.physics_thread.start()

        if os.getenv("MUJOCO_VIEWER", "false") == "true":
            self.viewer_thread = threading.Thread(target=self._launch_viewer)
            self.viewer_thread.daemon = True
            self.viewer_thread.start()

    def _physics_loop(self):
        dt = self.m.opt.timestep 
        while True:
            step_start = time.time()
            
            # Usamos o lock aqui para proteger o mj_step
            with self._lock:
                mujoco.mj_step(self.m, self.d)
            
            elapsed = time.time() - step_start
            if elapsed < dt:
                time.sleep(dt - elapsed)

    def _launch_viewer(self):
        with mujoco.viewer.launch_passive(self.m, self.d) as v:32
            while v.is_running():
                # Protege a cópia dos dados para o visualizador
                with self._lock:
                    v.sync()
                time.sleep(0.01) 

    def update_joints(self, joints_in_rad: dict):
        # Também usamos o lock aqui para atualizar o ctrl com segurança
        with self._lock:
            for name, value in joints_in_rad.items():
                if name in JOINT_INDEX:
                    indice = JOINT_INDEX[name]
                    min_val = self.m.jnt_range[indice][0]
                    max_val = self.m.jnt_range[indice][1]
                    target_pos = np.clip(value, min_val, max_val)
                    
                    self.d.ctrl[indice] = float(target_pos)
        
        print(f"Comandos atualizados: {list(joints_in_rad.values())}")