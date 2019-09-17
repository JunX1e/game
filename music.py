import time
import pygame



def play(ztime):

    file=r'music/jinitaimei.mp3'
    pygame.mixer.init()
         # print("播放音乐1")

    track = pygame.mixer.music.load(file)

    pygame.mixer.music.play()
    time.sleep(ztime)
    pygame.mixer.music.stop()



def clock(ztime):
    time_set = ztime
    sysj = None

    start_time = time.time()

    while True:
       t1 = time.time() - start_time
       sysj = time_set - t1

       if sysj > 0 :
            print(sysj)
       else:
            print("end")