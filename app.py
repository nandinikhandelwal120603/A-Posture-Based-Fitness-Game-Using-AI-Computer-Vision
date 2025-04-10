
# from flask import Flask, render_template, Response, request, redirect, url_for
# import threading
# import cv2
# import time
# import random

# # Import all the game logic classes
# from game_1 import Game1
# from game_2 import Game2
# from game_3 import Game3
# from game_4 import Game4
# from game_5 import Game5
# from game_6 import Game6

# app = Flask(__name__)

# # =========================
# # GLOBAL GAME STATE
# # =========================
# current_game = None
# scoreboard = {}

# # Game instances
# game_instances = {
#     'squat': Game1(),
#     'crunch': Game2(),
#     'raise': Game3(),
#     'neck': Game4(),
#     'beast': Game5(),
#     'coreburn': Game6()
# }

# # =========================
# # Webcam Feed Generator (routes through active game)
# # =========================
# def gen():
#     cap = cv2.VideoCapture(0)
#     while True:
#         success, frame = cap.read()
#         if not success:
#             break

#         if current_game in game_instances:
#             game = game_instances[current_game]
#             frame = game.update(frame)

#         ret, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/video_feed')
# def video_feed():
#     return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/select/<game_name>')
# def select_game(game_name):
#     global current_game
#     current_game = game_name
#     return redirect(url_for('game_view'))

# @app.route('/game')
# def game_view():
#     return render_template('game.html', game=current_game)

# @app.route('/score/<game>/<int:points>')
# def update_score(game, points):
#     global scoreboard
#     scoreboard[game] = scoreboard.get(game, 0) + points
#     return {'score': scoreboard[game]}

# # =========================
# # MAIN
# # =========================
# if __name__ == '__main__':
#     app.run(debug=True)


# =========================
# FITNESS ARCADE UI + GAME MANAGER (FINAL INTEGRATED VERSION)
# =========================

# from flask import Flask, render_template, Response, request, redirect, url_for
# import threading
# import cv2
# import time
# import random
# import pygame

# # Import all the game logic classes
# from game_1 import Game1  # Squat Smash
# from game_2 import Game2  # Core Burn Blitz
# from game_3 import Game3  # Fruit Ninja Game
# from game_4 import Game4  # Crush Quest
# from game_5 import Game5  # Raise & Raise
# from game_6 import Game6  # Neck Defender

# app = Flask(__name__)

# # =========================
# # GLOBAL GAME STATE
# # =========================
# current_game = None
# scoreboard = {}
# rep_count = 0
# exercise_duration = 30

# # Initialize Pygame Mixer for audio
# pygame.mixer.init()
# def play_intro():
#     pygame.mixer.music.load('static/audio/intro.mp3')
#     pygame.mixer.music.play()

# # Game instances
# # With ✨ Hot Girl Energy ✨ names
# game_instances = {
#     'little_miss_squat': Game1(),       # Squat Smash
#     'core_blitz_babe': Game2(),         # Core Burn Blitz
#     'fruit_ninja_queen': Game3(),       # Fruit Ninja
#     'crush_quest_cutie': Game4(),       # Crush Quest
#     'raise_and_glow': Game5(),          # Raise & Raise
#     'neck_defender_diva': Game6()       # Neck Defender
# }

# # 💪 Combo Mode Options
# combo_sets = {
#     'combo_1': ['little_miss_squat', 'fruit_ninja_queen', 'neck_defender_diva'],
#     'combo_2': ['core_blitz_babe', 'raise_and_glow', 'crush_quest_cutie'],
#     'combo_3': ['neck_defender_diva', 'fruit_ninja_queen', 'core_blitz_babe'],
#     'combo_4': ['little_miss_squat', 'crush_quest_cutie', 'raise_and_glow'],
#     'combo_5': ['core_blitz_babe', 'little_miss_squat', 'neck_defender_diva'],
#     'combo_6': ['fruit_ninja_queen', 'crush_quest_cutie', 'raise_and_glow']
# }

# # =========================
# # Webcam Feed Generator (routes through active game)
# # =========================
# def gen():
#     cap = cv2.VideoCapture(0)
#     while True:
#         success, frame = cap.read()
#         if not success:
#             break

#         if current_game in game_instances:
#             game = game_instances[current_game]
#             frame = game.update(frame)
#             bg_path = f'static/backgrounds/bg_{current_game}.png'
#             try:
#                 bg = cv2.imread(bg_path)
#                 if bg is not None:
#                     frame = cv2.addWeighted(frame, 0.7, bg, 0.3, 0)
#             except:
#                 pass

#         # Add timer overlay
#         cv2.putText(frame, f"Time: {int(time.time() % 60)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
#         ret, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/video_feed')
# def video_feed():
#     return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/')
# def home():
#     return render_template('home.html', combos=combo_sets.keys(), games=game_instances)

# @app.route('/select/<game_name>', methods=['GET', 'POST'])
# def select_game(game_name):
#     global current_game, rep_count, exercise_duration
#     current_game = game_name
#     if request.method == 'POST':
#         rep_count = int(request.form.get('reps', 10))
#         exercise_duration = int(request.form.get('duration', 30))
#         threading.Thread(target=run_single_game).start()
#         return redirect(url_for('game_view'))
#     return render_template('reps_input.html', game=game_name)

# def run_single_game():
#     global current_game
#     play_intro()
#     time.sleep(5)
#     game = game_instances[current_game]
#     game.reset()
#     time.sleep(exercise_duration)
#     current_game = None  # 👈 Don't reset this too early!


# @app.route('/game')
# def game_view():
#     combo_done = request.args.get('combo_done') == '1'
#     print("combo_done:", combo_done)
#     print("game:", current_game)

#     return render_template(
#         'game.html',
#         game=current_game,
#         combo_done=combo_done if combo_done is not None else ""
#         )



# @app.route('/score/<game>/<int:points>')
# def update_score(game, points):
#     global scoreboard
#     scoreboard[game] = scoreboard.get(game, 0) + points
#     return {'score': scoreboard[game]}

# @app.route('/combo/<combo_name>', methods=['GET', 'POST'])
# def start_combo(combo_name):
#     global current_game, rep_count, exercise_duration
#     combo_sequence = combo_sets.get(combo_name, [])

#     if request.method == 'POST':
#         rep_count = int(request.form.get('reps', 10))
#         exercise_duration = int(request.form.get('duration', 30))
#         threading.Thread(target=run_combo, args=(combo_sequence,)).start()
#         return redirect(url_for('game_view'))

#     return render_template('reps_input.html', game=combo_name, is_combo=True)

# def run_combo(sequence):
#     global current_game
#     for game in sequence:
#         current_game = game
#         play_intro()
#         time.sleep(15)  # Delay for intro
#         game_instance = game_instances[game]
#         if hasattr(game_instance, 'reset'):
#             game_instance.reset()
#         time.sleep(exercise_duration)
#         current_game = None
#         time.sleep(10)
       

#     current_game = None  # 👈 Do this only after ALL games


# # =========================
# # MAIN
# # =========================
# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, Response, request, redirect, url_for
# import threading
# import cv2
# import time
# import random
# import pygame

# # Import all the game logic classes
# from game_1 import Game1
# from game_2 import Game2
# from game_3 import Game3
# from game_4 import Game4
# from game_5 import Game5
# from game_6 import Game6

# app = Flask(__name__)

# # =========================
# # GLOBAL GAME STATE
# # =========================
# current_game = None
# scoreboard = {}
# rep_count = 0
# exercise_duration = 30
# timer_start = None  # ✅ NEW: Real timer tracking

# # Initialize Pygame Mixer for audio
# pygame.mixer.init()

# def play_intro():
#     pygame.mixer.music.load('static/audio/intro.mp3')
#     pygame.mixer.music.play()

# def play_final_song():  # ✅ NEW: Finale audio
#     pygame.mixer.music.load('static/audio/final_song.mp3')
#     pygame.mixer.music.play()

# # Game instances
# game_instances = {
#     'little_miss_squat': Game1(),
#     'core_blitz_babe': Game2(),
#     'fruit_ninja_queen': Game3(),
#     'crush_quest_cutie': Game4(),
#     'raise_and_glow': Game5(),
#     'neck_defender_diva': Game6()
# }

# combo_sets = {
#     'combo_1': ['little_miss_squat', 'fruit_ninja_queen', 'neck_defender_diva'],
#     'combo_2': ['core_blitz_babe', 'raise_and_glow', 'crush_quest_cutie'],
#     'combo_3': ['neck_defender_diva', 'fruit_ninja_queen', 'core_blitz_babe'],
#     'combo_4': ['little_miss_squat', 'crush_quest_cutie', 'raise_and_glow'],
#     'combo_5': ['core_blitz_babe', 'little_miss_squat', 'neck_defender_diva'],
#     'combo_6': ['fruit_ninja_queen', 'crush_quest_cutie', 'raise_and_glow']
# }

# def gen():
#     cap = cv2.VideoCapture(0)
#     global current_game, timer_start
#     while True:
#         success, frame = cap.read()
#         if not success:
#             break

#         if current_game in game_instances:
#             game = game_instances[current_game]
#             frame = game.update(frame)

#             bg_path = f'static/backgrounds/bg_{current_game}.png'
#             try:
#                 bg = cv2.imread(bg_path)
#                 if bg is not None:
#                     frame = cv2.addWeighted(frame, 0.7, bg, 0.3, 0)
#             except:
#                 pass

#         # ✅ Handle Timer Logic
#         if current_game and timer_start:
#             elapsed = time.time() - timer_start
#             remaining = max(0, exercise_duration - int(elapsed))

#             cv2.putText(frame, f"Time Left: {remaining}s", (10, 30),
#                         cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

#             # ⛔️ Time’s up? Shut it down
#             if remaining <= 0:
#                 print("⏰ Time's up! Ending game.")
#                 current_game = None
#                 timer_start = None
#                 play_final_song()
#                 # Optional: break camera feed here if needed
#                 # break

#         ret, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# @app.route('/video_feed')
# def video_feed():
#     return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/')
# def home():
#     return render_template('home.html', combos=combo_sets.keys(), games=game_instances)

# @app.route('/select/<game_name>', methods=['GET', 'POST'])
# def select_game(game_name):
#     global current_game, rep_count, exercise_duration, timer_start
#     current_game = game_name
#     if request.method == 'POST':
#         rep_count = int(request.form.get('reps', 10))
#         exercise_duration = int(request.form.get('duration', 30))
#         timer_start = time.time()  # ✅ Start timer
#         threading.Thread(target=run_single_game).start()
#         return redirect(url_for('game_view'))
#     return render_template('reps_input.html', game=game_name)

# def run_single_game():
#     global current_game
#     play_intro()
#     time.sleep(5)
#     game = game_instances[current_game]
#     game.reset()
#     time.sleep(exercise_duration)
#     current_game = None

# @app.route('/game')
# def game_view():
#     combo_done = request.args.get('combo_done') == '1'
#     print("combo_done:", combo_done)
#     print("game:", current_game)

#     return render_template(
#         'game.html',
#         game=current_game,
#         combo_done=combo_done if combo_done is not None else ""
#     )

# @app.route('/score/<game>/<int:points>')
# def update_score(game, points):
#     global scoreboard
#     scoreboard[game] = scoreboard.get(game, 0) + points
#     return {'score': scoreboard[game]}

# @app.route('/combo/<combo_name>', methods=['GET', 'POST'])
# def start_combo(combo_name):
#     global current_game, rep_count, exercise_duration, timer_start
#     combo_sequence = combo_sets.get(combo_name, [])

#     if request.method == 'POST':
#         rep_count = int(request.form.get('reps', 10))
#         exercise_duration = int(request.form.get('duration', 30))
#         timer_start = time.time()  # ✅ Start timer
#         threading.Thread(target=run_combo, args=(combo_sequence,)).start()
#         return redirect(url_for('game_view'))

#     return render_template('reps_input.html', game=combo_name, is_combo=True)

# def run_combo(sequence):
#     global current_game, timer_start
#     for game in sequence:
#         current_game = game
#         play_intro()
#         time.sleep(15)
#         game_instance = game_instances[game]
#         if hasattr(game_instance, 'reset'):
#             game_instance.reset()
#         timer_start = time.time()  # ✅ Reset timer per game
#         time.sleep(exercise_duration)
#         current_game = None
#         time.sleep(10)

#     timer_start = None
#     current_game = None
#     play_final_song()  # ✅ Finale Song Trigger

# if __name__ == '__main__':
#     app.run(debug=True)


# =========================
# FITNESS ARCADE UI + GAME MANAGER (FINAL INTEGRATED VERSION)
# =========================

# from flask import Flask, render_template, Response, request, redirect, url_for
# import threading
# import cv2
# import time
# import random
# import pygame

# # Import all the game logic classes
# from game_1 import Game1  # Squat Smash
# from game_2 import Game2  # Core Burn Blitz
# from game_3 import Game3  # Fruit Ninja Game
# from game_4 import Game4  # Crush Quest
# from game_5 import Game5  # Raise & Raise
# from game_6 import Game6  # Neck Defender

# app = Flask(__name__)

# # =========================
# # GLOBAL GAME STATE
# # =========================
# current_game = None
# scoreboard = {}
# rep_count = 0
# exercise_duration = 30

# # Initialize Pygame Mixer for audio
# pygame.mixer.init()
# def play_intro():
#     pygame.mixer.music.load('static/audio/intro.mp3')
#     pygame.mixer.music.play()

# # Game instances
# # With ✨ Hot Girl Energy ✨ names
# game_instances = {
#     'little_miss_squat': Game1(),       # Squat Smash
#     'core_blitz_babe': Game2(),         # Core Burn Blitz
#     'fruit_ninja_queen': Game3(),       # Fruit Ninja
#     'crush_quest_cutie': Game4(),       # Crush Quest
#     'raise_and_glow': Game5(),          # Raise & Raise
#     'neck_defender_diva': Game6()       # Neck Defender
# }

# # 💪 Combo Mode Options
# combo_sets = {
#     'combo_1': ['little_miss_squat', 'fruit_ninja_queen', 'neck_defender_diva'],
#     'combo_2': ['core_blitz_babe', 'raise_and_glow', 'crush_quest_cutie'],
#     'combo_3': ['neck_defender_diva', 'fruit_ninja_queen', 'core_blitz_babe'],
#     'combo_4': ['little_miss_squat', 'crush_quest_cutie', 'raise_and_glow'],
#     'combo_5': ['core_blitz_babe', 'little_miss_squat', 'neck_defender_diva'],
#     'combo_6': ['fruit_ninja_queen', 'crush_quest_cutie', 'raise_and_glow']
# }

# # =========================
# # Webcam Feed Generator (routes through active game)
# # =========================
# def gen():
#     cap = cv2.VideoCapture(0)
#     while True:
#         success, frame = cap.read()
#         if not success:
#             break

#         if current_game in game_instances:
#             game = game_instances[current_game]
#             frame = game.update(frame)
#             bg_path = f'static/backgrounds/bg_{current_game}.png'
#             try:
#                 bg = cv2.imread(bg_path)
#                 if bg is not None:
#                     frame = cv2.addWeighted(frame, 0.7, bg, 0.3, 0)
#             except:
#                 pass

#         # Add timer overlay
#         cv2.putText(frame, f"Time: {int(time.time() % 60)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
#         ret, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/video_feed')
# def video_feed():
#     return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/')
# def home():
#     return render_template('home.html', combos=combo_sets.keys(), games=game_instances)

# @app.route('/select/<game_name>', methods=['GET', 'POST'])
# def select_game(game_name):
#     global current_game, rep_count, exercise_duration
#     current_game = game_name
#     if request.method == 'POST':
#         rep_count = int(request.form.get('reps', 10))
#         exercise_duration = int(request.form.get('duration', 30))
#         threading.Thread(target=run_single_game).start()
#         return redirect(url_for('game_view'))
#     return render_template('reps_input.html', game=game_name)

# def run_single_game():
#     global current_game
#     play_intro()
#     time.sleep(5)  # Delay for intro
#     game = game_instances[current_game]
#     game.reset()
#     time.sleep(exercise_duration)
#     current_game = None

# @app.route('/game')
# def game_view():
#     return render_template('game.html', game=current_game)

# @app.route('/score/<game>/<int:points>')
# def update_score(game, points):
#     global scoreboard
#     scoreboard[game] = scoreboard.get(game, 0) + points
#     return {'score': scoreboard[game]}

# @app.route('/combo/<combo_name>', methods=['GET', 'POST'])
# def start_combo(combo_name):
#     global current_game, rep_count, exercise_duration
#     combo_sequence = combo_sets.get(combo_name, [])

#     if request.method == 'POST':
#         rep_count = int(request.form.get('reps', 10))
#         exercise_duration = int(request.form.get('duration', 30))
#         threading.Thread(target=run_combo, args=(combo_sequence,)).start()
#         return redirect(url_for('game_view'))

#     return render_template('reps_input.html', game=combo_name, is_combo=True)

# def run_combo(sequence):
#     global current_game
#     for game in sequence:
#         current_game = game
#         play_intro()
#         time.sleep(5)  # Delay for intro
#         game_instance = game_instances[game]
#         game_instance.reset()
#         time.sleep(exercise_duration)
#         current_game = None
#         time.sleep(10)  # Break
#     current_game = None

# # =========================
# # MAIN
# # =========================
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, Response, request, redirect, url_for, jsonify
import threading
import cv2
import time
import random
from datetime import datetime

# Import game logic classes
from game_1 import Game1
from game_2 import Game2
from game_3 import Game3
from game_4 import Game4
from game_5 import Game5
from game_6 import Game6

app = Flask(__name__)

# =========================
# GLOBAL GAME STATE
# =========================
current_game = None
scoreboard = {}
rep_count = 0
exercise_duration = 30
summary_data = None  # shared after workout ends

game_instances = {
    'little_miss_squat': Game1(),
    'core_blitz_babe': Game2(),
    'fruit_ninja_queen': Game3(),
    'crush_quest_cutie': Game4(),
    'raise_and_glow': Game5(),
    'neck_defender_diva': Game6()
}

combo_sets = {
    'combo_1': ['little_miss_squat', 'fruit_ninja_queen', 'neck_defender_diva'],
    'combo_2': ['core_blitz_babe', 'raise_and_glow', 'crush_quest_cutie'],
    'combo_3': ['neck_defender_diva', 'fruit_ninja_queen', 'core_blitz_babe'],
    'combo_4': ['little_miss_squat', 'crush_quest_cutie', 'raise_and_glow'],
    'combo_5': ['core_blitz_babe', 'little_miss_squat', 'neck_defender_diva'],
    'combo_6': ['fruit_ninja_queen', 'crush_quest_cutie', 'raise_and_glow']
}

def gen():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break

        if current_game in game_instances:
            game = game_instances[current_game]
            frame = game.update(frame)
            bg_path = f'static/backgrounds/bg_{current_game}.png'
            try:
                bg = cv2.imread(bg_path)
                if bg is not None:
                    frame = cv2.addWeighted(frame, 0.7, bg, 0.3, 0)
            except:
                pass

        # You had a fake timer display here, removed for clarity
        # cv2.putText(frame, f"Time: {int(time.time() % 60)}", (10, 30), ...)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def home():
    return render_template('home.html', combos=combo_sets.keys(), games=game_instances)

@app.route('/select/<game_name>', methods=['GET', 'POST'])
def select_game(game_name):
    global current_game, rep_count, exercise_duration
    current_game = game_name
    if request.method == 'POST':
        rep_count = int(request.form.get('reps', 10))
        exercise_duration = int(request.form.get('duration', 30))
        threading.Thread(target=run_single_game).start()
        return redirect(url_for('game_view'))
    return render_template('reps_input.html', game=game_name)

def run_single_game():
    global current_game, summary_data, rep_count, exercise_duration
    game = game_instances[current_game]
    total_calories = 0

    for i in range(rep_count):
        game.reset()
        start = time.time()
        while time.time() - start < exercise_duration:
            time.sleep(1)
        total_calories += 5  # placeholder
        if i < rep_count - 1:
            time.sleep(10)  # break

    summary_data = {
        "name": "Hot Girl",
        "game": current_game.replace('_', ' ').title(),
        "reps": rep_count,
        "calories": total_calories,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Cleanup state
    current_game = None
    rep_count = 0
    exercise_duration = 0

@app.route('/game')
def game_view():
    return render_template('game.html', game=current_game)

@app.route('/check_done')
def check_done():
    return jsonify({"done": summary_data is not None})

@app.route('/summary')
def summary():
    global summary_data, current_game, rep_count, exercise_duration
    if summary_data:
        log = summary_data
        summary_data = None
        current_game = None
        rep_count = 0
        exercise_duration = 0
        return render_template("summary.html", log=log)
    else:
        return redirect(url_for('home'))

@app.route('/score/<game>/<int:points>')
def update_score(game, points):
    global scoreboard
    scoreboard[game] = scoreboard.get(game, 0) + points
    return {'score': scoreboard[game]}

@app.route('/combo/<combo_name>', methods=['GET', 'POST'])
def start_combo(combo_name):
    global current_game, rep_count, exercise_duration
    combo_sequence = combo_sets.get(combo_name, [])

    if request.method == 'POST':
        rep_count = int(request.form.get('reps', 10))
        exercise_duration = int(request.form.get('duration', 30))
        threading.Thread(target=run_combo, args=(combo_sequence,)).start()
        return redirect(url_for('game_view'))

    return render_template('reps_input.html', game=combo_name, is_combo=True)

def run_combo(sequence):
    global current_game, summary_data, rep_count, exercise_duration

    total_reps = 0
    total_calories = 0

    for game_name in sequence:
        current_game = game_name
        game_instance = game_instances[game_name]

        for i in range(rep_count):
            game_instance.reset()
            start = time.time()
            while time.time() - start < exercise_duration:
                time.sleep(1)
            total_calories += 5
            total_reps += 1
            if i < rep_count - 1:
                time.sleep(10)  # break between reps

        time.sleep(10)  # break between games

    summary_data = {
        "name": "Hot Girl",
        "game": " + ".join([g.replace('_', ' ').title() for g in sequence]),
        "reps": total_reps,
        "calories": total_calories,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Cleanup
    current_game = None
    rep_count = 0
    exercise_duration = 0

if __name__ == '__main__':
    app.run(debug=True)
