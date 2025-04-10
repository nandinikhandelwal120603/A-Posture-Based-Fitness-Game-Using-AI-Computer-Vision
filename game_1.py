# import cv2
# import mediapipe as mp
# import numpy as np
# import random
# import os
# import tkinter as tk
# from tkinter import messagebox
# import tkinter as tk
# from tkinter import simpledialog, messagebox

# # Suppress TensorFlow warnings
# os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# # Initialize MediaPipe Hand tracking
# mp_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_utils
# hands = mp_hands.Hands(min_detection_confidence=0.7, max_num_hands=2)

# # Game window size
# WIDTH, HEIGHT = 640, 480

# # Racket and shuttlecock settings
# PLAYER_Y = HEIGHT - 50
# OPPONENT_Y = 50
# RACKET_WIDTH, RACKET_HEIGHT = 100, 20
# BALL_RADIUS = 10

# # Initialize shuttlecock position
# shuttle_x, shuttle_y = WIDTH // 2, HEIGHT // 2
# shuttle_vx, shuttle_vy = 0, 0  # Stays still until tossed

# # Player and opponent racket positions
# player_x = WIDTH // 2
# opponent_x = WIDTH // 2

# tossed = False  # Game starts only after shuttle is tossed
# player_score, opponent_score = 0, 0

# # Tkinter window for player names
# root = tk.Tk()
# root.withdraw()
# player_name = tk.simpledialog.askstring("Player Name", "Enter your name:")
# if not player_name:
#     player_name = "Player"

# cap = cv2.VideoCapture(0)

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         continue

#     frame = cv2.flip(frame, 1)  # Mirror the image
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     result = hands.process(rgb_frame)

#     fist_detected = False  # Track if a fist is detected

#     if result.multi_hand_landmarks:
#         for hand_landmarks in result.multi_hand_landmarks:
#             mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
#             wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
#             index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
#             pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

#             x_pos = int(wrist.x * WIDTH)
#             y_pos = int(wrist.y * HEIGHT)

#             # Check for fist (distance between index and pinky small)
#             if abs(index_tip.x - pinky_tip.x) < 0.05 and abs(index_tip.y - pinky_tip.y) < 0.05:
#                 fist_detected = True

#             # Left hand tosses the shuttle
#             if wrist.x < 0.5 and not tossed:
#                 shuttle_x, shuttle_y = x_pos, y_pos
#             else:
#                 player_x = x_pos

#     # Start game after shuttle is tossed
#     if shuttle_y < HEIGHT // 2 and not tossed:
#         tossed = True
#         shuttle_vy = 5  # Drop shuttle into play

#     # Move shuttlecock
#     shuttle_x += shuttle_vx
#     shuttle_y += shuttle_vy

#     # Ensure shuttlecock coordinates are integers
#     shuttle_x, shuttle_y = int(shuttle_x), int(shuttle_y)

#     # Collision with player's racket
#     if PLAYER_Y - BALL_RADIUS < shuttle_y < PLAYER_Y + RACKET_HEIGHT and abs(shuttle_x - player_x) < RACKET_WIDTH // 2:
#         shuttle_vy = -shuttle_vy
#         shuttle_vx = random.choice([-5, 5])
#         if fist_detected:
#             shuttle_vy -= 5  # Smash boost

#     # Collision with opponent's racket
#     if OPPONENT_Y < shuttle_y < OPPONENT_Y + RACKET_HEIGHT and abs(shuttle_x - opponent_x) < RACKET_WIDTH // 2:
#         shuttle_vy = -shuttle_vy
#         shuttle_vx = random.choice([-5, 5])

#     # Wall collision (left/right)
#     if shuttle_x <= BALL_RADIUS or shuttle_x >= WIDTH - BALL_RADIUS:
#         shuttle_vx = -shuttle_vx

#     # Score points if shuttlecock goes out of bounds
#     if shuttle_y > HEIGHT:
#         opponent_score += 1
#         tossed = False
#         shuttle_x, shuttle_y = WIDTH // 2, HEIGHT // 2
#         shuttle_vx, shuttle_vy = 0, 0
#     elif shuttle_y < 0:
#         player_score += 1
#         tossed = False
#         shuttle_x, shuttle_y = WIDTH // 2, HEIGHT // 2
#         shuttle_vx, shuttle_vy = 0, 0

#     # Check win condition
#     if player_score == 10:
#         messagebox.showinfo("Game Over", f"{player_name} wins!")
#         break
#     elif opponent_score == 10:
#         messagebox.showinfo("Game Over", "Opponent wins!")
#         break

#     # Move AI racket
#     if opponent_x < shuttle_x:
#         opponent_x += min(5, abs(opponent_x - shuttle_x))
#     elif opponent_x > shuttle_x:
#         opponent_x -= min(5, abs(opponent_x - shuttle_x))

#     # Draw player racket
#     cv2.rectangle(frame, (player_x - RACKET_WIDTH // 2, PLAYER_Y), (player_x + RACKET_WIDTH // 2, PLAYER_Y + RACKET_HEIGHT), (255, 0, 0), -1)
    
#     # Draw opponent racket
#     cv2.rectangle(frame, (opponent_x - RACKET_WIDTH // 2, OPPONENT_Y), (opponent_x + RACKET_WIDTH // 2, OPPONENT_Y + RACKET_HEIGHT), (0, 255, 0), -1)
    
#     # Draw shuttlecock
#     cv2.circle(frame, (shuttle_x, shuttle_y), BALL_RADIUS, (0, 255, 255), -1)
    
#     # Draw scores
#     cv2.putText(frame, f"{player_name}: {player_score}", (10, HEIGHT - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
#     cv2.putText(frame, f"Opponent: {opponent_score}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

#     # Display the game window
#     cv2.imshow("Badminton AI Game", frame)

#     key = cv2.waitKey(1) & 0xFF
#     if key == ord('q'):
#         break
#     elif key == ord('r'):
#         player_score, opponent_score = 0, 0  # Reset both scores
#         tossed = False
#         shuttle_x, shuttle_y = WIDTH // 2, HEIGHT // 2
#         shuttle_vx, shuttle_vy = 0, 0


# cap.release()
# cv2.destroyAllWindows()
# game_1.py - Squat Smash Game

import cv2
import mediapipe as mp
import numpy as np
import random

class Game1:
    def __init__(self):
        self.width, self.height = 640, 480
        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.7)
        self.colors = [(255, 0, 255), (0, 255, 255), (255, 255, 0), (0, 255, 0)]
        self.score = 0
        self.target = self.spawn_target()

    def spawn_target(self):
        x = random.randint(100, self.width - 100)
        y = random.randint(100, self.height - 200)
        size = 40
        color = random.choice(self.colors)
        return {'x': x, 'y': y, 'size': size, 'hit': False, 'color': color}

    def reset(self):
        """Reset game state — like a fresh start after rage quitting 😤🎮"""
        self.score = 0
        self.target = self.spawn_target()

    def update(self, frame):
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(rgb_frame)

        if not self.target['hit']:
            cv2.rectangle(frame, 
                          (self.target['x'] - self.target['size'], self.target['y'] - self.target['size']),
                          (self.target['x'] + self.target['size'], self.target['y'] + self.target['size']),
                          self.target['color'], -1)

        if results.pose_landmarks:
            self.mp_drawing.draw_landmarks(frame, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)

            # Get hip position (landmark 24 for right hip)
            hip_x = int(results.pose_landmarks.landmark[24].x * self.width)
            hip_y = int(results.pose_landmarks.landmark[24].y * self.height)

            if not self.target['hit'] and abs(hip_x - self.target['x']) < self.target['size'] and abs(hip_y - self.target['y']) < self.target['size']:
                self.target['hit'] = True
                self.score += 1
                self.target = self.spawn_target()

        cv2.putText(frame, f'Score: {self.score}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        return frame

