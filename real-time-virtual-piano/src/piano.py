import pygame
import cv2
import numpy as np

class VirtualPiano:
    def __init__(self):
        self.piano_keys = {"C": "assets/piano_sounds/C.wav", "D": "assets/piano_sounds/D.wav", "E": "assets/piano_sounds/E.wav"}
        self.overlay = cv2.imread("assets/piano_overlay.png")
        
    def draw_piano_overlay(self, frame):
        overlay_resized = cv2.resize(self.overlay, (frame.shape[1], 100))
        frame[-100:, :] = overlay_resized
        return frame
    
    def get_pressed_key(self, landmarks):
        for x, y in landmarks:
            if y > 400:
                return "C"
        return None
    
    def play_sound(self, key):
        if key in self.piano_keys:
            pygame.mixer.Sound(self.piano_keys[key]).play()
