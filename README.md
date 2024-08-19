# 📸 Face Recognition Attendance System
# 📝 Overview
This project is a Face Recognition Attendance System built using Python, OpenCV, and the face_recognition library. The system is designed to automatically detect and recognize faces from a webcam feed and mark attendance by logging the name of the recognized individual along with the time of recognition. It is ideal for schools, offices, or any organization where automated attendance is required.

# 🚀 Features
Real-time Face Recognition: Detects and recognizes faces using your webcam.

Attendance Logging: Logs the name and time of recognized individuals into a CSV file.

Easy to Extend: Simply add more images to expand the recognition database.

# 🛠️ How It Works
Image Collection: Store images of individuals in the ImagesAttendance folder. Each image should be named with the individual's name (e.g., John_Doe.jpg).

Face Encoding: The system extracts facial features from these images and stores them as encodings for recognition.

Recognition & Logging: The webcam captures frames, detects faces, and compares them with the stored encodings. Recognized faces are logged in Attendance.csv with the current time.
