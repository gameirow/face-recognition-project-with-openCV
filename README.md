# face-recognition-project-with-openCV

# Overview
This project is a Face Recognition Attendance System built using Python, OpenCV, and the face_recognition library. The system is designed to automatically detect and recognize faces from a webcam feed and mark attendance by logging the name of the recognized individual along with the time of recognition. The project can be extended and integrated into a larger attendance management system for schools, offices, or any organization where automated attendance is required.

# Features
Real-time Face Recognition: Uses your webcam to detect and recognize faces in real-time.
Attendance Logging: Automatically logs the attendance of recognized individuals into a CSV file with their name and the time of recognition.
Easy to Extend: Easily add more images to expand the recognition database.
How It Works
Image Collection: The system uses a folder named ImagesAttendance where you store images of the individuals you want to recognize. Each image should be named with the individual's name (e.g., John_Doe.jpg).

Face Encoding: The system processes the images, extracts facial features, and stores them as encodings. These encodings are used to recognize faces in the webcam feed.

Recognition and Attendance Logging: During runtime, the webcam captures frames, detects faces, and compares them against the known encodings. If a face is recognized, the system logs the person's name and the current time in Attendance.csv.
