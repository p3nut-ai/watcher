import time, cv2
from threading import Thread
from djitellopy import Tello

tello = Tello()
record = True
tello.streamon()
frame_read = tello.get_frame_read()
#tello.streamon()
def ai_flight():
    height, width, _ = frame.read.frame.shape

    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while record:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()


def start_record(target=ai_flight):
    recorder = Thread(target=target)
    recorder.start()

    tello.takeoff()
    tello.move_up(100)
    tello.rotate_counter_clockwise(360)
    tello.land()

    keepRecording = False
    recorder.join()

