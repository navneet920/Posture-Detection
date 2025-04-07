Body Posture Detection with Pose Estimation
rust
Copy
Edit

HEAD -> User Input Form -> Greeting -> Database Setup -> Pose Detection & Analysis -> Data Logging -> End -> NULL
🔗 Node 1: User Input Form (GUI using Tkinter)
Collects user details:

Name

Age

Gender

Phone Number

Email

Validates all fields before allowing the posture detection process to begin.

Used to customize data logging per user.

🔗 Node 2: Greeting (Text-to-Speech)
Uses pyttsx3 to greet the user with:

"Welcome to the posture detection model"

🔗 Node 3: Database Setup (sqlite3)
Creates a database user_pose_data.db.

Each user has a unique table: user_<name>.

Table stores:

Timestamp

Image path

Age, Gender

Phone and Email

🔗 Node 4: Pose Detection (OpenCV + MediaPipe)
Live webcam feed is captured using cv2.VideoCapture(0).

Uses mediapipe pose module to extract key landmarks.

Calculates angles at:

Left & Right Elbow

Left & Right Knee

🔗 Node 5: Data Logging
Every 10 seconds for 3 minutes:

Captures image

Overlays angles

Saves image in saved_images/<user_name>/

Logs timestamp and metadata in the database

🔗 Node 6: End Process
Webcam feed ends after 3 minutes or if 'q' is pressed.

Final speech: "Thank you"

Closes all resources.

⚙️ Dependencies
Install the following before running:

bash
Copy
Edit
pip install opencv-python mediapipe numpy pyttsx3
📂 Folder Structure
python
Copy
Edit
project_root/
│
├── saved_images/
│   └── user_name/
│       └── image files with timestamps
│
├── user_pose_data.db    # SQLite database
└── your_script.py       # The Python file shown above
🚀 How to Run
bash
Copy
Edit
python your_script.py
Make sure your webcam is enabled and accessible.

📝 Notes
Image capture is silent in the background.

You can expand this project by:

Adding emotion detection

Classifying good vs bad posture

Sending posture feedback via SMS/email

Would you like this README as a downloadable .md file or in another format?







You said:
on github


ChatGPT said:
Great! Here's a GitHub-ready README.md file for your Body Posture Detection using Pose Estimation project. You can copy-paste it into your repository’s README.md or upload it directly.

markdown
Copy
Edit
# 🧍‍♂️ Body Posture Detection using Pose Estimation

This project captures a user's posture using their webcam and analyzes key body angles using **MediaPipe**. It stores periodic screenshots and user metadata into a local **SQLite** database.

---

## 🧠 Project Flow (Like a Linked List)

HEAD -> User Input Form -> Greeting -> Database Setup -> Pose Detection & Analysis -> Data Logging -> End -> NULL

yaml
Copy
Edit

---

## 📌 Features

- 📋 GUI form to collect user info
- 🗣️ Text-to-speech greeting & exit
- 🎯 Real-time pose detection using MediaPipe
- 📸 Auto-saves posture images every 10 seconds
- 🗃️ Logs posture data in an SQLite database
- 🧾 Organized folder structure per user

---

## 📦 Dependencies

Install all required Python packages:

```bash
pip install opencv-python mediapipe numpy pyttsx3
Also includes standard libraries: tkinter, sqlite3, os, csv, time, datetime.

🚀 How to Run
Clone the repository or download the project folder.

Open a terminal and run:

bash
Copy
Edit
python your_script.py
Fill out the form that appears.

Posture detection will run for 3 minutes, saving an image every 10 seconds.

Press q anytime to quit early.

🗂️ Folder Structure
bash
Copy
Edit
project_root/
│
├── saved_images/
│   └── <user_name>/
│       └── <timestamp>.jpg
│
├── user_pose_data.db    # SQLite database
└── your_script.py       # Main Python file
🧮 Key Angles Tracked
Left and Right Elbow

Left and Right Knee

These angles are calculated and shown on the image during live tracking.

🧠 Future Scope
Classify posture as Good or Bad

Send real-time feedback via SMS/email

Add emotion detection using face landmarks

Export captured data for ML model training

🛡️ Disclaimer
This model is intended for research and educational purposes only.

🙌 Author
Navneet Kumar

vbnet
Copy
Edit

Let me know if you want help uploading it to GitHub or making a repository logo/banner!






You said:
more descriptive


ChatGPT said:
Absolutely! Here's a more detailed and descriptive version of the README.md file that would look great on your GitHub project page. This version includes expanded explanations, visuals (with placeholders), and detailed instructions for both usage and contribution.

markdown
Copy
Edit
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

> *(Add GIF or image of your application running here)*  
> Example:  
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
