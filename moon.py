#!/usr/bin/python

from time import sleep
import pygame
import keyboard

def play_sound(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def main():
    sound_file_bg = "/home/moon/service/moon_bg.mp3" 
    sound_file_en = "/home/moon/service/moon_en.mp3"

    while True:
        try:
            if keyboard.is_pressed('Page_Down'):
                print("starting bg, page down")
                play_sound(sound_file_bg)
                keyboard.wait('Page_Down')  # Wait for the key release to avoid continuous triggering
            if keyboard.is_pressed('Page_Up'):
                print("starting en, page up")
                play_sound(sound_file_en)
                keyboard.wait('Page_Up')  # Wait for the key release to avoid continuous triggering
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
