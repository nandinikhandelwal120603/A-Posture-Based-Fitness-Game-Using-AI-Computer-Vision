# Crunch Quest (Belly/Abs) Game
# File: crunch_quest.py
import cv2
import mediapipe as mp

class Game4:
    def __init__(self):
        self.rep_count = 0
        self.state = "down"
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()

    def update(self, frame):
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(image_rgb)

        if results.pose_landmarks:
            left_shoulder = results.pose_landmarks.landmark[11]
            left_hip = results.pose_landmarks.landmark[23]
            distance = abs(left_shoulder.y - left_hip.y)

            if distance < 0.1 and self.state == "down":
                self.state = "up"
                self.rep_count += 1
            elif distance > 0.2:
                self.state = "down"

        cv2.putText(frame, f"Crunches: {self.rep_count}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

        return frame