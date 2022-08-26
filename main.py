import time
from djitellopy import Tello
from manual_drive import manual_drive
from ai_flight import ai_flight
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
    # print('----------------------------------------------------')
    print('\n')
    print('Battery: {}'.format(tello.get_battery()) + '/100')
    print('Temp: {}'.format(tello.get_temperature()))

except Exception as e:

    print('\n')
    print(Fore.RED + '[-] Connection error [-]')
    quit()



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
    ai_flight()
else:
    print(Fore.RED + '[!] not in the choices [!]')
