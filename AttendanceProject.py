import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# Set the path to the directory containing images for attendance
path = 'ImagesAttendance'
images = []  # List to store loaded images
classNames = []  # List to store the names of the people in the images
myList = os.listdir(path)  # Get a list of all files in the directory
print(myList)

# Loop through each file in the directory and load the image and its corresponding name
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')  # Read the image
    images.append(curImg)  # Add the image to the images list
    classNames.append(os.path.splitext(cl)[0])  # Add the name (without file extension) to classNames

print(classNames)

# Function to find and return face encodings for a list of images
def findEncodings(images):
    encodeList = []  # List to store the face encodings
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert the image to RGB format
        encode = face_recognition.face_encodings(img)[0]  # Get the face encoding for the image
        encodeList.append(encode)  # Add the encoding to the list
    return encodeList

# Function to mark attendance by writing the person's name and time to a CSV file
def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:  # Open the CSV file in read and append mode
        myDataList = f.readlines()  # Read all lines in the file
        nameList = []  # List to store the names already recorded
        for line in myDataList:
            entry = line.split(',')  # Split each line by comma
            nameList.append(entry[0])  # Add the first element (name) to the nameList
        if name not in nameList:  # Check if the name is not already recorded
            now = datetime.now()  # Get the current date and time
            dtString = now.strftime('%H:%M:%S')  # Format the time as a string
            f.writelines(f'\n{name}, {dtString}')  # Write the name and time to the file

# Find and store encodings for all known images
encodeListKnown = findEncodings(images)
print('Encoding Complete')

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()  # Capture a frame from the webcam
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)  # Resize the image to 1/4th size for faster processing
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)  # Convert the image to RGB format

    facesCurFrame = face_recognition.face_locations(imgS)  # Detect faces in the current frame
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)  # Get face encodings for the detected faces

    # Loop through each face found in the current frame
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)  # Compare the face with known encodings
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)  # Compute the distance between faces
        # print(faceDis)
        matchIndex = np.argmin(faceDis)  # Find the index of the closest match

        if matches[matchIndex]:  # If the closest match is a valid match
            name = classNames[matchIndex].upper()  # Get the name of the matched person
            # print(name)
            y1, x2, y2, x1 = faceLoc  # Get the location of the face
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4  # Scale the face location back up to the original size
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Draw a rectangle around the face
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)  # Draw a filled rectangle for the name label
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)  # Write the name below the face
            markAttendance(name)  # Call the function to mark attendance for the identified person

    cv2.imshow('Webcam', img)  # Display the webcam feed with annotations
    cv2.waitKey(1)  # Wait for 1 ms before moving to the next frame; this also allows breaking the loop by pressing a key

#to add other images to be identified, you simply move them to the "images attendance" folder