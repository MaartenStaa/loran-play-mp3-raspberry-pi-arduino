#!/usr/bin/env python3

# Before running, make sure to run: pip3 install -r requirements.txt
import pygame
import serial

ARDUINO_SERIAL_DEVICE = '/dev/ttyACM0'
# Try .ogg files if .mp3 doesn't work
TRACK_FILE_0 = '/home/track0.mp3'
TRACK_FILE_1 = '/home/track1.mp3'
MUSIC_VOLUME = 1.0
FADE_IN_OUT_MS = 500

pygame.mixer.init()
pygame.mixer.music.set_volume(MUSIC_VOLUME)

def play_song(track):
    if track == 0:
        track_file = TRACK_FILE_0
    else:
        track_file = TRACK_FILE_1

    # Remove if you don't want a fadeout
    pygame.mixer.music.fadeout(time = FADE_IN_OUT_MS)
    pygame.mixer.music.load(track_file)
    pygame.mixer.music.play(fade_ms = FADE_IN_OUT_MS)

if __name__ == '__main__':
    ser = serial.Serial(ARDUINO_SERIAL_DEVICE, 9600, timeout = 1)
    ser.reset_input_buffer()

    last_signal = None

    while True:
        if ser.in_waiting > 0:
            # Read one line of utf-8 formatted text. This may need to
            # change if the Arduino is sending individual characters without
            # any line breaks in between.
            line = ser.readline().decode('utf-8').rstrip()
            if line != last_signal:
                print(f'Received {signal} from Arduino')
                play_song(line)
                last_signal = line
