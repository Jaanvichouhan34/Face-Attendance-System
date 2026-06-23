# Face Attendance Management System

A robust, real-time facial recognition attendance system with a graphical user interface. This project utilizes deep learning models (MTCNN for face detection and FaceNet for facial embeddings) to accurately track and record student attendance.

## Features

- **Real-Time Detection:** Live video feed facial recognition using MTCNN and FaceNet.
- **Automated Tracking:** Automatically logs the exact entry time, exit time, and total duration for each person.
- **Local Database:** Uses SQLite to store attendance session records reliably.
- **Graphical Interface:** Easy-to-use GUI built with Tkinter.
- **Reporting:** View daily attendance summaries and export all data to CSV files.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Jaanvichouhan34/Face-Attendance-System.git
   cd Face-Attendance-System
   ```

2. **Install the dependencies:**
   Make sure you have Python installed. Run the following command in the root directory:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

**Important:** You must navigate into the `src` folder before running the application, otherwise it will fail to find the local database and models!

1. Open your terminal or command prompt.
2. Navigate into the source directory:
   ```bash
   cd src
   ```
3. Run the GUI:
   ```bash
   python gui.py
   ```

### GUI Options
- **Start Attendance:** Opens the webcam and begins logging attendance. Press **Escape (Esc)** or **Q** to close the camera window. *Closing the window correctly is required to force-save your session!*
- **View Report:** Displays a summary of total duration and times for the day.
- **View Database:** Opens a table viewing all raw attendance records.
- **Export CSV:** Dumps the database into an Excel-friendly CSV file in the `reports` folder.

## Technologies Used

- `Python 3`
- `TensorFlow` & `Keras-FaceNet` (Embeddings)
- `MTCNN` (Face Detection)
- `OpenCV` (Computer Vision / Webcam capture)
- `SQLite3` (Database)
- `Tkinter` (GUI)
