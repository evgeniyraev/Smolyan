#!/usr/bin/python

from time import sleep
import pygame
import keyboard
import threading
import signal
import sys
#from motorControl import *
from mockMottor import *
from webControll import start_web_intergace

def set_audio_output():
    pygame.mixer.init()

def play_sound(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(3.2)
    cw() 
    

def stop_sound():
    pygame.mixer.music.stop()
    #stop_rotation()

def listen_end_sound():
    while True:
        if pygame.mixer.music.get_busy() == False and isRotating() == True:
            stop_rotation()
            sleep(0.1)

def listen_end_sound_thead():
    thread = threading.Thread(target=listen_end_sound)
    thread.deamon = True
    thread.start()

def play_sound_thread(file_path):
    thread = threading.Thread(target=play_sound, args=(file_path,))
    thread.deamon = True
    thread.start()
    
    


def main():
    pygame.mixer.init()
    #start_web_intergace()
    listen()
    listen_end_sound_thead()

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

            elif keyboard.is_pressed("F5") or keyboard.is_pressed("Esc"):
                print("unhadeled")
                sleep(0.1)
            
            elif keyboard.is_pressed('space') or keyboard.is_pressed("."):
                print("stopping")
                stop_sound()
                #stop_rotation()
                sleep(0.1)


        except KeyboardInterrupt:
            break

def signal_term_handler(signal, frame):
    print('got SIGTERM')
    sys.exit(0)

signal.signal(signal.SIGTERM, signal_term_handler)

if __name__ == "__main__":
    main()
