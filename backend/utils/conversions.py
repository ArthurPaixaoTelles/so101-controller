JOINT_LIMITS = {
    "shoulder_pan":  {"min": -1.9199, "max":  1.9199},
    "shoulder_lift": {"min": -1.7453, "max":  1.7453},
    "elbow_flex":    {"min": -1.69,   "max":  1.69},
    "wrist_flex":    {"min": -1.6581, "max":  1.6581},
    "wrist_roll":    {"min": -2.7438, "max":  2.8412},
    "gripper":       {"min": -0.1745, "max":  1.7453},
}

def servo_to_rad(value, min_rad, max_rad):
    return min_rad + (value / 4095.0) * (max_rad - min_rad)