# a face recognition project
# importing the necessary libraries
import cv2
import numpy as np
import face_recognition

#importing the images
imgElon = face_recognition.load_image_file('venv/elon musk test image 2 sub 3.jpg')
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('venv/Bill_Gates test image.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

#step 2: finding the faces in our images, and then finding their encodings as well
faceLoc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255,0,255), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255,0,255), 2)


#testing if the 2 images are from the same person or not
results = face_recognition.compare_faces([encodeElon], encodeTest) #tells if it is true or false (match or no match)
faceDis = face_recognition.face_distance([encodeElon], encodeTest) #shows in number the likeliness of being a match
print(results, faceDis) #THE lower the distance, more likely it is to be a match, 0 being perfect match. usually, below 0.6 is a match
cv2.putText(imgTest, f'{results} {round(faceDis[0], 2)}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)

cv2.imshow('elon musk test image', imgElon)
cv2.imshow('elon_musk_test image 2', imgTest)
cv2.waitKey(0)