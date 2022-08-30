import time
from djitellopy import Tello
from manual_drive import manual_drive
from colorama import Fore
from threading import Thread
import cv2

try:
    tello = Tello()
    tello.connect()
    print(Fore.CYAN + "[*] Connecting ...")
    time.sleep(1)
    print(Fore.GREEN + "[+] Connection established [+]")
    time.sleep(1)
    print(Fore.WHITE + '----------------------------------------------------')
    print(Fore.WHITE + '''

               _..:::.._
             .:::::/|::::.
           ::::::/ V|::::::
          ::::::/'  |::::::   Watcher (dji trello)
          ::::<_,   (::::::      By: Jonathan J.
           :::::|    \::::
            '::/      \:'

        ''')
    # print('----------------------------------------------------')
    print('\n')
    print('Battery: {}'.format(tello.get_battery()) + '/100')
    print('Temp: {}'.format(tello.get_temperature()))

except Exception as e:

    print('\n')
    print(Fore.RED + '[-] Connection error [-]')
    quit()


print('''
        ------------------------------------

        (1) Manual flight
        (2) Ai flight

        -----------------------------------
        ''')

user_choice = input('> ')



if user_choice == '1':
    # call function from other py file
    manual_drive()
    
elif user_choice == '2':
    record = True
    tello.streamon()
    frame_read = tello.get_frame_read()

    def ai_flight():


        height, width, _ = frame_read.frame.shape

        video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

        while record:
            video.write(frame_read.frame)
            time.sleep(1 / 30)
        video.release()

    recorder = Thread(target=ai_flight)
    recorder.start()

    if tello.get_battery() < 20:
        print(Fore.YELLOW + "[!] WARNING! [!]")
        print(Fore.RED + "[!] Battery is low [!]")
    else:
        tello.takeoff()
        #tello.move_up(100)
        tello.rotate_counter_clockwise(360)
        tello.land()
        #time.sleep(2)
        record = False
        recorder.join()



else:
    print(Fore.RED + '[!] not in the choices [!]')
