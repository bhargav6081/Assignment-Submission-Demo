import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    flag, frame = cap.read()

    if not flag:
      print("Could not access the camera.")
      # If loading a video, use 'break' instead of 'continue'.
      break
    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)

    frame.flags.writeable = False
    results = hands.process(frame)
    # Draw the hand annotations on the image.
    frame.flags.writeable = True
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            frame, landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow('Frame' , frame)
    if cv2.waitKey(10) & 0xff == ord('q'):
      break
cap.release()
cv2.destroyAllWindows()