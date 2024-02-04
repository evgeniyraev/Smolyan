#!/usr/bin/python

from time import sleep
import pygame
import keyboard
import threading

def set_audio_output():
    pygame.mixer.init()

def play_sound(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_sound():
    pygame.mixer.music.stop()

def play_sound_thread(file_path):
    thread = threading.Thread(target=play_sound, args=(file_path,))
    thread.start()

def main():
    pygame.mixer.init()

    sound_file_bg = "/home/moon/service/moon_bg.mp3" 
    sound_file_en = "/home/moon/service/moon_en.mp3"

    while True:
        try:
            if keyboard.is_pressed('Page_Down'):
                print("starting bg, page down")
                stop_sound()
                play_sound_thread(sound_file_bg)
                sleep(0.1)

            elif keyboard.is_pressed('Page_Up'):
                print("starting en, page up")
                stop_sound()
                play_sound_thread(sound_file_en)
                sleep(0.1)

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
