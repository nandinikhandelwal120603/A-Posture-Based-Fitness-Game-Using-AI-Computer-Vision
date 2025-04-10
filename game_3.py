
# # import cv2
# # import mediapipe as mp
# # import numpy as np
# # import random

# # # Initialize Mediapipe Hand Detection
# # mp_hands = mp.solutions.hands
# # mp_drawing = mp.solutions.drawing_utils
# # hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# # # Game variables
# # width, height = 640, 480
# # fruit = None  # Only one fruit
# # score = 0
# # fruit_types = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0)]  # Different colors for fruits

# # def spawn_fruit():
# #     x = random.randint(100, width - 100)
# #     y = height  # Start from bottom
# #     speed = random.randint(5, 10)
# #     color = random.choice(fruit_types)
# #     return {'x': x, 'y': y, 'speed': speed, 'hit': False, 'color': color}

# # fruit = spawn_fruit()

# # cap = cv2.VideoCapture(0)

# # while cap.isOpened():
# #     ret, frame = cap.read()
# #     if not ret:
# #         break
    
# #     frame = cv2.flip(frame, 1)
# #     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# #     results = hands.process(rgb_frame)
    
# #     # Draw fruit
# #     if not fruit['hit']:
# #         cv2.circle(frame, (fruit['x'], fruit['y']), 30, fruit['color'], -1)
# #         fruit['y'] -= fruit['speed']  # Move fruit upwards
# #         if fruit['y'] < 0:
# #             fruit = spawn_fruit()  # Respawn if missed
    
# #     # Hand detection
# #     if results.multi_hand_landmarks:
# #         for hand_landmarks in results.multi_hand_landmarks:
# #             mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
# #             # Get fist position (knuckles - landmarks 9 & 13)
# #             x1, y1 = int(hand_landmarks.landmark[9].x * width), int(hand_landmarks.landmark[9].y * height)
# #             x2, y2 = int(hand_landmarks.landmark[13].x * width), int(hand_landmarks.landmark[13].y * height)
# #             fist_center = ((x1 + x2) // 2, (y1 + y2) // 2)
            
# #             # Check for fruit collision
# #             if not fruit['hit'] and (fruit['x'] - fist_center[0])**2 + (fruit['y'] - fist_center[1])**2 < 1600:
# #                 fruit['hit'] = True
# #                 score += 1
# #                 fruit = spawn_fruit()  # Spawn new fruit
    
# #     # Show score
# #     cv2.putText(frame, f'Score: {score}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
# #     cv2.imshow('Fruit Punch Game', frame)
    
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break

# # cap.release()
# # cv2.destroyAllWindows()

# import cv2
# import mediapipe as mp
# import numpy as np
# import random

# # Initialize Mediapipe Hand Detection
# mp_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_utils
# hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# # Game variables
# width, height = 640, 480
# fruit = None  # Only one fruit
# score = 0

# def spawn_fruit(hand='right'):
#     x = random.randint(100, width - 100)
#     y = height  # Start from bottom
#     speed = random.randint(5, 10)
#     color = (0, 255, 0) if hand == 'right' else (0, 0, 255)  # Green for right hand, Red for left hand
#     return {'x': x, 'y': y, 'speed': speed, 'hit': False, 'color': color, 'hand': hand}

# fruit = spawn_fruit()

# cap = cv2.VideoCapture(0)

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
    
#     frame = cv2.flip(frame, 1)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     results = hands.process(rgb_frame)
    
#     # Draw fruit
#     if not fruit['hit']:
#         cv2.circle(frame, (fruit['x'], fruit['y']), 30, fruit['color'], -1)
#         fruit['y'] -= fruit['speed']  # Move fruit upwards
#         if fruit['y'] < 0:
#             fruit = spawn_fruit(random.choice(['right', 'left']))  # Respawn for random hand
    
#     # Hand detection
#     if results.multi_hand_landmarks:
#         for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
#             mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
#             hand_label = handedness.classification[0].label.lower()  # 'Right' or 'Left'
            
#             # Get fist position (knuckles - landmarks 9 & 13)
#             x1, y1 = int(hand_landmarks.landmark[9].x * width), int(hand_landmarks.landmark[9].y * height)
#             x2, y2 = int(hand_landmarks.landmark[13].x * width), int(hand_landmarks.landmark[13].y * height)
#             fist_center = ((x1 + x2) // 2, (y1 + y2) // 2)
            
#             # Check for fruit collision
#             if not fruit['hit'] and fruit['hand'] == hand_label and (fruit['x'] - fist_center[0])**2 + (fruit['y'] - fist_center[1])**2 < 1600:
#                 fruit['hit'] = True
#                 score += 1
#                 fruit = spawn_fruit(random.choice(['right', 'left']))  # Spawn new fruit
    
#     # Show score
#     cv2.putText(frame, f'Score: {score}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
#     cv2.imshow('Fruit Punch Game', frame)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2
import mediapipe as mp
import numpy as np
import random
import time

class Game3:
    def __init__(self):
        self.width, self.height = 640, 480
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
        self.fruit = self.spawn_fruit()
        self.score = 0
        self.start_time = time.time()
        self.countdown_done = False

    def reset(self):
        self.fruit = self.spawn_fruit()
        self.score = 0
        self.start_time = time.time()
        self.countdown_done = False

    def spawn_fruit(self, hand='right'):
        x = random.randint(100, self.width - 100)
        y = self.height
        speed = random.randint(5, 10)
        color = (0, 255, 0) if hand == 'right' else (0, 0, 255)
        return {'x': x, 'y': y, 'speed': speed, 'hit': False, 'color': color, 'hand': hand}

    def update(self, frame):
        frame = cv2.flip(frame, 1)

        # Countdown logic before game starts
        elapsed = time.time() - self.start_time
        if not self.countdown_done:
            countdown = 3 - int(elapsed)
            if countdown > 0:
                cv2.putText(frame, str(countdown), (self.width // 2 - 50, self.height // 2), 
                            cv2.FONT_HERSHEY_DUPLEX, 4, (0, 0, 255), 5)
                return frame
            else:
                self.countdown_done = True

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)

        if not self.fruit['hit']:
            cv2.circle(frame, (self.fruit['x'], self.fruit['y']), 30, self.fruit['color'], -1)
            self.fruit['y'] -= self.fruit['speed']
            if self.fruit['y'] < 0:
                self.fruit = self.spawn_fruit(random.choice(['right', 'left']))

        if results.multi_hand_landmarks:
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                hand_label = handedness.classification[0].label.lower()
                x1, y1 = int(hand_landmarks.landmark[9].x * self.width), int(hand_landmarks.landmark[9].y * self.height)
                x2, y2 = int(hand_landmarks.landmark[13].x * self.width), int(hand_landmarks.landmark[13].y * self.height)
                fist_center = ((x1 + x2) // 2, (y1 + y2) // 2)

                if not self.fruit['hit'] and self.fruit['hand'] == hand_label and (self.fruit['x'] - fist_center[0]) ** 2 + (self.fruit['y'] - fist_center[1]) ** 2 < 1600:
                    self.fruit['hit'] = True
                    self.score += 1
                    self.fruit = self.spawn_fruit(random.choice(['right', 'left']))

        cv2.putText(frame, f'Score: {self.score}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        return frame
