from datetime import datetime
import time
import pygame


def sound():
    pygame.mixer.init()  # This init() function is to initialize all the "pygame.mixer" modules
    pygame.mixer.music.load("cm punk.mp3")


def alarm():
    hour = int(input("Enter the hour:"))
    minn = int(input("Enter the minute:"))
    sec = int(input("Enter the second:"))

    n = 3

    print("YOUR ALARM SET FOR", str(hour), ":", str(minn), ":", str(sec))
    while True:
        if time.localtime().tm_hour == hour and time.localtime().tm_min == minn and time.localtime().tm_sec == sec:
            print("WAKE UP!!!!!")
            break
    sound()

    while n > 0:
        pygame.mixer.music.play()
        time.sleep(10)
        n = n - 1

    sn = str(input("Press s for snooze\n>>"))
    if sn == "s":
        n = 3
        time.sleep(100)
        while n > 0:
            pygame.mixer.music.play()
            time.sleep(10)
    else:
        exit()


alarm()


