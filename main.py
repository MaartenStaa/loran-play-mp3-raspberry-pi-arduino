#!/usr/bin/env python3

# Before running, make sure to run: pip3 install -r requirements.txt
import pygame
import serial
import RPi.GPIO as io

TRACK_FILE_0 = '/home/pi/Music/Verkeerwav.wav'
TRACK_FILE_1 = '/home/pi/Music/Vogelswav.wav'
MUSIC_VOLUME = 1.0

io.setmode(io.BCM)
io.setup(2, io.IN)

pygame.mixer.init()
pygame.mixer.music.set_volume(MUSIC_VOLUME)

actual_last_signal = None
last_signal = None

while True:
    actual_signal = io.input(17)
    signal = io.input(17) > 0.5
    if signal != last_signal:
        print(f"Signal changed from {actual_last_signal} to {actual_signal}")
        if signal == False:
            track_file = TRACK_FILE_0
        else:
            track_file = TRACK_FILE_1

        pygame.mixer.music.load(track_file)
        pygame.mixer.music.play()
        actual_last_signal = actual_signal
        last_signal = signal
