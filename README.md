# 🕹️ Posture-based Game App – "Slay Time"

This project is a fun, interactive browser-based fitness game that tracks your body movements using your webcam. Using computer vision and AI, it challenges you to perform different neck or body exercises – and automatically tracks your reps!

## 🎯 What It Does

- Streams your webcam video live in-browser
- Uses MediaPipe (by Google) to detect facial landmarks
- Tracks specific movement patterns (like neck turns)
- Counts reps in real-time
- Ends session and shows a summary screen automatically

## 🛠️ Technologies Used

| Tech | Purpose |
|------|---------|
| Python (Flask) | Backend web server |
| HTML/CSS/JavaScript | Frontend UI |
| OpenCV | Image processing |
| MediaPipe | Face and pose tracking |
| Jinja2 | HTML templating |
| Threading | Real-time game loop |
| Bootstrap (optional) | Styling UI |

## 🧠 Methodology

1. Start a Flask web app that handles routes and webcam feed
2. Stream webcam frames and process them with OpenCV & MediaPipe
3. Extract landmark data to detect movement (like neck turning)
4. Update rep count, timer, and game state dynamically
5. Frontend polls backend to check if game is over
6. Redirects to summary page when done

## 🕹️ Game Modes Implemented

- **Neck Defender** (neck rotations – left ↔️ right)

You can add more games like squats, shoulder rolls, etc., by defining new classes.

## ▶️ How To Run

### Step 1: Clone the repo
```bash
git clone https://github.com/your-username/slay-time
cd slay-time
```

Step 2: Install requirements
```bash
pip install -r requirements.txt
```
Step 3: Run the app
```bash
python app.py
```
Then go to: http://127.0.0.1:5000

💡 Make sure your webcam is connected!
