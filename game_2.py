# import cv2
# import mediapipe as mp
# import numpy as np
# import random

# # Initialize Mediapipe Pose Detection
# mp_pose = mp.solutions.pose
# mp_drawing = mp.solutions.drawing_utils
# pose = mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# # Game variables
# width, height = 640, 480
# object_falling = None  # Only one falling object
# score = 0
# colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0)]

# def spawn_object():
#     x = random.randint(100, width - 100)
#     y = 0  # Start from the top
#     speed = random.randint(5, 10)
#     color = random.choice(colors)
#     return {'x': x, 'y': y, 'speed': speed, 'hit': False, 'color': color}

# object_falling = spawn_object()

# cap = cv2.VideoCapture(0)

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
    
#     frame = cv2.flip(frame, 1)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     results = pose.process(rgb_frame)
    
#     # Draw falling object
#     if not object_falling['hit']:
#         cv2.circle(frame, (object_falling['x'], object_falling['y']), 30, object_falling['color'], -1)
#         object_falling['y'] += object_falling['speed']  # Move object down
#         if object_falling['y'] > height:
#             object_falling = spawn_object()  # Respawn if missed
    
#     # Pose detection
#     if results.pose_landmarks:
#         mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        
#         # Get knee position (landmark 26 for right knee, 25 for left knee)
#         knee_x = int(results.pose_landmarks.landmark[26].x * width)
#         knee_y = int(results.pose_landmarks.landmark[26].y * height)
        
#         # Check for collision
#         if not object_falling['hit'] and (object_falling['x'] - knee_x)**2 + (object_falling['y'] - knee_y)**2 < 1600:
#             object_falling['hit'] = True
#             score += 1
#             object_falling = spawn_object()  # Spawn new object
    
#     # Show score
#     cv2.putText(frame, f'Score: {score}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
#     cv2.imshow('Lower Belly Workout Game', frame)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
# game_6.py - Core Burn Blitz
# =========================

import cv2
import mediapipe as mp
import numpy as np
import random

class Game2:
    def __init__(self):
        self.width, self.height = 640, 480
        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.7)
        self.colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0)]
        self.object = self.spawn_object()
        self.score = 0

    def spawn_object(self):
        x = random.randint(100, self.width - 100)
        y = 0
        speed = random.randint(5, 10)
        color = random.choice(self.colors)
        return {'x': x, 'y': y, 'speed': speed, 'hit': False, 'color': color}

    def update(self, frame):
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(rgb_frame)

        if not self.object['hit']:
            cv2.circle(frame, (self.object['x'], self.object['y']), 30, self.object['color'], -1)
            self.object['y'] += self.object['speed']
            if self.object['y'] > self.height:
                self.object = self.spawn_object()

        if results.pose_landmarks:
            self.mp_drawing.draw_landmarks(frame, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
            knee_x = int(results.pose_landmarks.landmark[26].x * self.width)
            knee_y = int(results.pose_landmarks.landmark[26].y * self.height)

            if not self.object['hit'] and (self.object['x'] - knee_x) ** 2 + (self.object['y'] - knee_y) ** 2 < 1600:
                self.object['hit'] = True
                self.score += 1
                self.object = self.spawn_object()

        cv2.putText(frame, f'Score: {self.score}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        return frame
