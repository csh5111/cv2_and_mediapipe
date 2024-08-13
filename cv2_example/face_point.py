import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)


mpDraw = mp.solutions.drawing_utils
mpFaces = mp.solutions.face_mesh
faceMesh = mpFaces.FaceMesh(max_num_faces=1)
# max_num_faces=1

while True:
    damn,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = faceMesh.process(imgRGB)
    # print(result.multi_face_landmarks)
    if result.multi_face_landmarks:
        for facelms in result.multi_face_landmarks:
            mpDraw.draw_landmarks(img,facelms)
        # ,FACE_CONNECTIONS,,mpFacseMesh
    flip = cv2.flip(img, 1)
    cv2.imshow('damn', flip)
    # cv2.imshow('damn',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        cap.release()                    #按‘q’键退出后，释放摄像头资源

        cv2.destroyAllWindows()
