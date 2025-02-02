import cv2
import pygame
import numpy as np
from src.hand_tracker import HandTracker
from src.piano import VirtualPiano

pygame.mixer.init()

hand_tracker = HandTracker()
virtual_piano = VirtualPiano()

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    hand_landmarks = hand_tracker.get_hand_landmarks(frame)
    frame = virtual_piano.draw_piano_overlay(frame)
    
    if hand_landmarks:
        key_pressed = virtual_piano.get_pressed_key(hand_landmarks)
        if key_pressed:
            virtual_piano.play_sound(key_pressed)
    
    cv2.imshow("Real-Time Virtual Piano", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
