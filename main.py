import time, cv2
from threading import Thread
from djitellopy import Tello
from manual_drive import manual_drive
from colorama import Fore



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
    print('----------------------------------------------------')
    print('\n')
    print('Battery: {}'.format(tello.get_battery()) + '/100')
    print('Temp: {}'.format(tello.get_temperature()))

except Exception as e:

    print('\n')
    print(Fore.RED + '[-] Connection error [-]')
    quit()

def ai_flight():

    # work here
    
    # tello.for_back_velocity = 0
    # tello.left_right_velocity = 0
    # tello.up_down_velocity = 0
    # tello.yawn_velocity = 0
    # tello.speed = 0
    # print('Battery: {}'.format(tello.get_battery()) + '/100')
    tello.streamoff()
    tello.streamon()



    w,h = 960,720

    # img H and W frame
    tello_frame = tello.get_frame_read()
    tello_frame = tello_frame.frame


    while True:
        img = cv2.resize(tello_frame,(w,h))

        cv2.imshow('img',img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            tello.land()
            break








# let user pick
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
    tello.takeoff()
    ai_flight()

else:
    print(Fore.RED + '[!] not in the choices [!]')

