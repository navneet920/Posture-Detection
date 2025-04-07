# 🧍‍♂️ AI-Based Body Posture Detection System using MediaPipe & OpenCV

This Python-based application is designed to **analyze human posture in real-time** using a webcam. It combines **MediaPipe Pose Estimation**, **OpenCV**, and a GUI built with **Tkinter** to capture the user's body angles, store periodic snapshots, and log data into an SQLite database for further analysis or ML training.

---

## 🔥 Key Features

✅ **User-Friendly GUI** to collect personal data (Name, Age, Gender, Phone, Email)  
✅ **Text-to-Speech** interaction to greet and thank the user  
✅ **Pose Estimation with MediaPipe** for accurate body keypoint detection  
✅ **Automated Image Capture** every 10 seconds for 3 minutes  
✅ **Angle Overlay** on joints like elbows and knees  
✅ **Local SQLite Database Logging** with timestamped records  
✅ **Organized Image Storage** under `saved_images/<user_name>/`  
✅ **CSV-ready Data Format** for ML and analytics tasks

---

## 🖼️ Demo Preview

> ![image](https://github.com/user-attachments/assets/1c6ddc77-4c3d-4374-bb3c-534630c4e14a)
 
> ![pose-demo](https://user-images.githubusercontent.com/your_image_url/demo.gif)

---

## ⚙️ Tech Stack

- **Language**: Python 3.x  
- **Libraries Used**:
  - [`mediapipe`](https://google.github.io/mediapipe/)
  - [`opencv-python`](https://pypi.org/project/opencv-python/)
  - `numpy`, `sqlite3`, `pyttsx3`, `tkinter`, `os`, `datetime`

---

## 🧭 Workflow Breakdown

### 1️⃣ User Input Form (GUI)
A simple Tkinter GUI pops up when the script runs, asking for the user’s personal information. This ensures personalized tracking and unique dataset generation.

### 2️⃣ Audio Welcome
A warm voice greets the user using `pyttsx3` and sets the tone for a user-friendly experience.

### 3️⃣ Real-time Pose Detection
- Uses MediaPipe to detect 33 key body landmarks.
- Calculates joint angles:
  - Left/Right Elbow
  - Left/Right Knee
- Displays angles live on the video feed.

### 4️⃣ Periodic Capture
- Images are captured every 10 seconds for a total of 3 minutes.
- Each image is saved to a user-specific folder and logged with metadata.

### 5️⃣ Database Logging
A new table is created in `user_pose_data.db` for each user. Each entry logs:
- Image path
- Timestamp
- User info (age, gender, phone, email)

### 6️⃣ Audio Goodbye
After the session ends, the system thanks the user via voice and exits gracefully.

---

## 📂 Directory Structure

project_root/ ├── your_script.py ├── user_pose_data.db ├── saved_images/ │ └── <user_name>/ │ └── 2025-04-07_10-15-00.jpg

yaml
Copy
Edit

---

## 🛠️ Installation

Ensure you have Python 3.10 or above. Then install required packages:

```bash
pip install opencv-python mediapipe numpy pyttsx3
For GUI support on some Linux distros, make sure tkinter is installed.

🚀 How to Run
bash
Copy
Edit
python your_script.py
Controls:
q → Quit the session early

Runs for 180 seconds (3 minutes) by default

📈 Future Enhancements
 Classify posture as "Good" or "Bad"

 Integrate feedback system via SMS/Email

 Export data to CSV for model training

 Add emotion detection using face landmarks

 Support for mobile and Raspberry Pi deployments

🙋 Author
Navneet Kumar
📧 Feel free to reach out or contribute!

🤝 Contributing
Want to make this better?
Fork the repo → Create a branch → Add your feature → Submit a PR ✅

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
