#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import mediapipe as mp
import pyautogui
import time
import datetime

def count_fingers(lst):
    cnt = 0
    thresh = (lst.landmark[0].y * 100 - lst.landmark[9].y * 100) / 2
    if (lst.landmark[5].y * 100 - lst.landmark[8].y * 100) > thresh: 
        cnt += 1
    if (lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > thresh: 
        cnt += 1
    if (lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > thresh: 
        cnt += 1
    if (lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[5].y * 100 - lst.landmark[4].y * 100) > 5: # Thumb
        cnt += 1
    return cnt

def rescale(frame, scale=0.2):
    width = int(3 * frame.shape[1] * scale)
    height = int(3 * frame.shape[0] * scale)
    dimension = (width, height)
    return cv2.resize(frame, dimension, interpolation=cv2.INTER_AREA)

cap = cv2.VideoCapture(0) 
drawing = mp.solutions.drawing_utils 
hands = mp.solutions.hands 
hand_obj = hands.Hands(max_num_hands=2) 

start_init = False
prev = -1

while True:
    end_time = time.time()
    ret, frm = cap.read()
    if not ret:
        break
    frm = cv2.flip(frm, 1)
    frm = cv2.resize(frm, (1000, 800))
    frm = cv2.copyMakeBorder(frm, 15, 15, 15, 15, cv2.BORDER_CONSTANT, value=0)
    res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    text = f'Height: {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}   Width: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}'
    date_data = f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    frm = cv2.putText(frm, text, (20, 50), font, 2, (0, 0, 0), 2)
    frm = cv2.putText(frm, date_data, (60, 90), font, 2, (0, 0, 0), 2)

    if res.multi_hand_landmarks:
        hand_keyPoints = res.multi_hand_landmarks[0]
        cnt = count_fingers(hand_keyPoints)
        if prev != cnt:
            if not start_init:
                start_time = time.time()
                start_init = True
            elif (end_time - start_time) > 0.3:
                if cnt == 1:
                    pyautogui.press("right")
                elif cnt == 2:
                    pyautogui.press("left")
                elif cnt == 3:
                    pyautogui.press("up")
                elif cnt == 4:
                    pyautogui.press("down")
                elif cnt == 5:
                    pyautogui.press("space")
                prev = cnt
                start_init = False
        
        drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)
        
    cv2.imshow('Hand Gesture Screen', rescale(frm))
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        cap.release()
        cv2.waitKey(0)
        break


# In[ ]:




