import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


while True:
    damn,img = cap.read()
    if damn:
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    # print(result.multi_hand_landmarks)
    if result.multi_hand_landmarks:
        for handlms in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,handlms)
        

    cv2.imshow('damn',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        cap.release()                    #按‘q’键退出后，释放摄像头资源

        cv2.destroyAllWindows()
