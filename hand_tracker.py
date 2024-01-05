#Import the libraries
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils  #makes interconnecting lines between landmarks
mp_drawing_styles = mp.solutions.drawing_styles

mphands = mp.solutions.hands

cap = cv2.VideoCapture(0)
hands = mphands.Hands()
while True:
    data,image = cap.read()
    #Flip the image
    image = cv2.cvtColor(cv2.flip(image, 1),cv2.COLOR_BGR2RGB)
    #Stores results
    results=hands.process(image)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,mphands.HAND_CONNECTIONS)
    cv2.imshow('HandTracker', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()