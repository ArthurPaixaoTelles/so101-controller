import { useState } from 'react';

function JointControl(){
const [joints,setJoints] = useState({
        shoulder_pan: 0,
        shoulder_lift: 0,
        elbow_flex: 0,
        wrist_flex: 0,
        wrist_roll: 0,
        gripper: 0
})

function handleChange(name, value) {
    setJoints({
        ...joints,
        [name]: value  
    })
}
function sendJoints(){
    fetch('http://localhost:8000/joints',{
        method:'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(joints)
    })

}
    return(<div>
            <label htmlFor="shoulder_pan">Shoulder Pan: {joints.shoulder_pan}</label>
            <input type="range" id="shoulder_pan" min="0" max= "4095" value={joints.shoulder_pan} onChange={e => {handleChange("shoulder_pan", e.target.value); sendJoints();}}  ></input>
            <label htmlFor="shoulder_lift">Shoulder Lift: {joints.shoulder_lift}</label>
            <input type="range" id="shoulder_lift" min="0" max= "4095" value={joints.shoulder_lift} onChange={e => {handleChange("shoulder_lift", e.target.value); sendJoints();}} sendJoints></input>            
            <label htmlFor="elbow_flex">Elbow Flex: {joints.elbow_flex}</label>
            <input type="range" id="elbow_flex" min="0" max= "4095" value={joints.elbow_flex} onChange={e => {handleChange("elbow_flex", e.target.value); sendJoints();}} sendJoints></input>
            <label htmlFor="wrist_flex">Wrist Flex: {joints.wrist_flex}</label>
            <input type="range" id="wrist_flex" min="0" max= "4095" value={joints.wrist_flex} onChange={e => {handleChange("wrist_flex", e.target.value); sendJoints();}} sendJoints></input>
            <label htmlFor="wrist_roll">Wrist Roll: {joints.wrist_roll}</label>
            <input type="range" id="wrist_roll" min="0" max= "4095" value={joints.wrist_roll} onChange={e => {handleChange("wrist_roll", e.target.value); sendJoints();}} sendJoints></input>
            <label htmlFor="gripper">Gripper: {joints.gripper}</label>
            <input type="range" id="gripper" min="0" max= "4095" value={joints.gripper} onChange={e => {handleChange("gripper", e.target.value); sendJoints();}} sendJoints></input>

    </div>) 

}

export default JointControl