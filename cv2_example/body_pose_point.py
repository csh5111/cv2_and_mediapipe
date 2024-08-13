import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpPose = mp.solutions.pose
# min_detection_confidence=0.8,min_tracking_confidence=0.5
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

while True:
    damn, img = cap.read()
    if damn:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = pose.process(imgRGB)
    print(result.pose_landmarks)
    # .multi_pose_landmarks
    if result.pose_landmarks:
    #     for poselms in result.multi_pose_landmarks:
            mpDraw.draw_landmarks(img,result.pose_landmarks )
    #poselms, mpPose.POSE_CONNECTIONS
    # flip = cv2.flip(img, 1)
    # cv2.imshow('damn', flip)
    cv2.imshow('damn',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        cap.release()  # 按‘q’键退出后，释放摄像头资源

        cv2.destroyAllWindows()
