from fastapi import APIRouter
from pydantic import BaseModel
from simulation import Simulation
from utils.conversions import servo_to_rad, JOINT_LIMITS
sim = Simulation()
router = APIRouter()
class JointsCommand(BaseModel):
    shoulder_pan: float
    shoulder_lift: float
    elbow_flex: float
    wrist_flex: float
    wrist_roll:float
    gripper:float
current_joints = {
    "shoulder_pan": 0,
    "shoulder_lift": 0,
    "elbow_flex": 0,
    "wrist_flex": 0,
    "wrist_roll": 0,
    "gripper": 0
}
@router.get("/joints")
def get_joints():
    return current_joints
@router.post("/joints")
def update_joints(command: JointsCommand):
    current_joints.update(command.dict())
    joints_in_rad = {}
    for name, value in command.dict().items():
        limits = JOINT_LIMITS[name]
        joints_in_rad[name] = servo_to_rad(value, limits["min"], limits["max"])
    sim.update_joints(joints_in_rad)
    print("joints em radianos:", joints_in_rad)
    return current_joints  