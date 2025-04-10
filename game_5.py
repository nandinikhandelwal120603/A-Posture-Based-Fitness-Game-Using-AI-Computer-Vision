# Raise Raid (Shoulder) Game
# File: raise_raid.py
import cv2
import mediapipe as mp

class Game5:
    def __init__(self):
        self.rep_count = 0
        self.state = "down"
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()

    def update(self, frame):
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(image_rgb)

        if results.pose_landmarks:
            left_wrist = results.pose_landmarks.landmark[15]
            left_shoulder = results.pose_landmarks.landmark[11]

            if left_wrist.y < left_shoulder.y and self.state == "down":
                self.state = "up"
                self.rep_count += 1
            elif left_wrist.y > left_shoulder.y:
                self.state = "down"

        cv2.putText(frame, f"Shoulder Raises: {self.rep_count}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        return frame