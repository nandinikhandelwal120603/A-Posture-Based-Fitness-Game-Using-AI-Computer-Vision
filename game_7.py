# Beast Mode 60 (Jumping Jacks HIIT-style)
# File: beast_mode_60.py
import cv2
import mediapipe as mp
class BeastMode60:
    def __init__(self):
        self.rep_count = 0
        self.state = "in"
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()

    def update(self, frame):
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(image_rgb)

        if results.pose_landmarks:
            left_ankle = results.pose_landmarks.landmark[27]
            right_ankle = results.pose_landmarks.landmark[28]

            distance = abs(left_ankle.x - right_ankle.x)
            if distance > 0.5 and self.state == "in":
                self.state = "out"
                self.rep_count += 1
            elif distance < 0.3:
                self.state = "in"

        cv2.putText(frame, f"Jumping Jacks: {self.rep_count}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        return frame
