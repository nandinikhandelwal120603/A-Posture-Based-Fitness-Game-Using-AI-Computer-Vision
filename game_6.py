# Neck Defender (Neck Rotations) Game
# File: neck_defender.py
import cv2
import mediapipe as mp

class Game6:
    def __init__(self):
        self.rep_count = 0
        self.state = "center"
        self.mp_face = mp.solutions.face_mesh
        self.face = self.mp_face.FaceMesh()

    def update(self, frame):
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face.process(image_rgb)

        if results.multi_face_landmarks:
            face_landmarks = results.multi_face_landmarks[0]
            nose_tip = face_landmarks.landmark[1]

            if nose_tip.x < 0.45 and self.state != "left":
                self.state = "left"
                self.rep_count += 1
            elif nose_tip.x > 0.55 and self.state != "right":
                self.state = "right"
                self.rep_count += 1
            elif 0.45 <= nose_tip.x <= 0.55:
                self.state = "center"

        cv2.putText(frame, f"Neck Turns: {self.rep_count}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 100, 255), 2)

        return frame

    def reset(self):
        self.rep_count = 0
        self.state = "center"
