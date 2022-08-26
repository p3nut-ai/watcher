from djitellopy import Tello
import pygame
import numpy as np
import cv2
import time 

tello = Tello()

def ai_flight():

    # work here
    FPS = 120
    pygame.init()
    screen = pygame.display.set_mode([960, 720])
    tello.streamoff()
    tello.streamon()


    tello_frame = tello.get_frame_read()

    should_stop = False
    while not should_stop:

        for event in pygame.event.get():
            if event.type == pygame.USEREVENT + 1:
                update()
            elif event.type == pygame.QUIT:
                should_stop = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    should_stop = True
                else:
                    keydown(event.key)
            elif event.type == pygame.KEYUP:
                keyup(event.key)

        if tello_frame.stopped:
            break

        screen.fill([0, 0, 0])

        frame = tello_frame.frame

                # text = "Battery: {}%".format(self.tello.get_battery())
                # cv2.putText(frame, text, (5, 720 - 5),
                #     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = np.flipud(frame)

        frame = pygame.surfarray.make_surface(frame)
        screen.blit(frame, (0, 0))
        pygame.display.update()

        time.sleep(1 / FPS)
