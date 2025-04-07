import cv2
import mediapipe as mp
import numpy as np
import tkinter as tk
from tkinter import messagebox
import csv
import os
import time
from datetime import datetime
import sqlite3
import pyttsx3  # For audio greeting

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 130)


def speak(text):
    engine.say(text)
    engine.runAndWait()

# ======================= GUI FORM ==========================
user_data = {}

def submit_form():
    user_data['name'] = name_var.get().strip().replace(' ', '_')  # for DB/table name
    user_data['age'] = age_var.get()
    user_data['gender'] = gender_var.get()
    user_data['phone'] = phone_var.get()
    user_data['email'] = email_var.get()

    if not all(user_data.values()):
        messagebox.showwarning("Incomplete Form", "Please fill in all fields.")
        return

    root.destroy()  # Close the form and proceed

# Create GUI
root = tk.Tk()
root.title("User Details Form")
root.geometry("400x300")

tk.Label(root, text="Enter Your Details", font=('Arial', 16)).pack(pady=10)

name_var = tk.StringVar()
age_var = tk.StringVar()
gender_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()

tk.Label(root, text="Name").pack()
tk.Entry(root, textvariable=name_var).pack()
tk.Label(root, text="Age").pack()
tk.Entry(root, textvariable=age_var).pack()
tk.Label(root, text="Gender").pack()
tk.Entry(root, textvariable=gender_var).pack()
tk.Label(root, text="Phone Number").pack()
tk.Entry(root, textvariable=phone_var).pack()
tk.Label(root, text="Email ID").pack()
tk.Entry(root, textvariable=email_var).pack()
tk.Button(root, text="Submit", command=submit_form).pack(pady=10)

root.mainloop()

# Speak welcome message
speak("Welcome to the posture detection model")

# =================== DATABASE SETUP ===================
conn = sqlite3.connect("user_pose_data.db")
cursor = conn.cursor()

# Create a table specific to this user
table_name = f"user_{user_data['name']}"
cursor.execute(f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    timestamp TEXT,
    image_path TEXT,
    age TEXT,
    gender TEXT,
    phone TEXT,
    email TEXT
)
""")
conn.commit()

# ======================= Pose Detection ==========================
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def calculate_angle(a, b, c):
    a, b, c = np.array(a), np.array(b), np.array(c)
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - \
              np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    return int(360 - angle) if angle > 180.0 else int(angle)

# Create image output folder
output_folder = f"saved_images/{user_data['name']}"
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(0)

start_time = time.time()
last_capture_time = start_time
duration = 180  # 3 minutes
capture_interval = 10  # 10 seconds

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time > duration:
            messagebox.showinfo("Time Limit", "Your time limit has ended.")
            break

        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        image = cv2.resize(frame, (1280, 720))
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_rgb.flags.writeable = False
        results = pose.process(image_rgb)
        image_rgb.flags.writeable = True
        image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

        try:
            landmarks = results.pose_landmarks.landmark
            h, w, _ = image.shape
            get_point = lambda lm: (int(landmarks[lm].x * w), int(landmarks[lm].y * h))

            angles_to_display = [
                (mp_pose.PoseLandmark.LEFT_SHOULDER, mp_pose.PoseLandmark.LEFT_ELBOW, mp_pose.PoseLandmark.LEFT_WRIST),
                (mp_pose.PoseLandmark.RIGHT_SHOULDER, mp_pose.PoseLandmark.RIGHT_ELBOW, mp_pose.PoseLandmark.RIGHT_WRIST),
                (mp_pose.PoseLandmark.LEFT_HIP, mp_pose.PoseLandmark.LEFT_KNEE, mp_pose.PoseLandmark.LEFT_ANKLE),
                (mp_pose.PoseLandmark.RIGHT_HIP, mp_pose.PoseLandmark.RIGHT_KNEE, mp_pose.PoseLandmark.RIGHT_ANKLE),
            ]

            for a, b, c in angles_to_display:
                pt1, pt2, pt3 = get_point(a), get_point(b), get_point(c)
                angle = calculate_angle(pt1, pt2, pt3)
                cv2.putText(image, str(angle), pt2, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

        except:
            pass

        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=4),
                                  mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=2))

        # Save image every 10 seconds
        if current_time - last_capture_time >= capture_interval:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"{timestamp}.jpg"
            filepath = os.path.join(output_folder, filename)
            cv2.imwrite(filepath, image)

            # Save to database
            cursor.execute(f"""
                INSERT INTO {table_name} (timestamp, image_path, age, gender, phone, email)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (timestamp, filepath, user_data['age'], user_data['gender'], user_data['phone'], user_data['email']))
            conn.commit()

            print(f"[INFO] Saved {filepath}")
            last_capture_time = current_time

        cv2.imshow("Pose Detection", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
conn.close()
cv2.destroyAllWindows()

# Speak thank you
speak("Thank you")
