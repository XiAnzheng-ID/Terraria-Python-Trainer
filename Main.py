import sys
import subprocess
import ctypes
import os
import time

ctypes.windll.kernel32.SetConsoleTitleW("Terraria v1.4.4.9 Trainer by XiAnzheng , Enjoy :D ")
os.system("cls")
print('Checking required module....')
time.sleep(2)
try:
    from ReadWriteMemory import ReadWriteMemory
    from ReadWriteMemory import ReadWriteMemoryError
    print('Required module is installed')
    time.sleep(2)
    os.system('cls')

except ModuleNotFoundError:
    print('Required module is NOT installed!!!')
    print('Installing Required Module....')

    python = sys.executable
    subprocess.check_call(
        [python, '-m', 'pip', 'install', 'ReadWriteMemory'],
        stdout=subprocess.DEVNULL
    )

finally:
    from ReadWriteMemory import ReadWriteMemory
    from ReadWriteMemory import ReadWriteMemoryError

rwm = ReadWriteMemory()
try:
    process = rwm.get_process_by_name("Terraria.exe") #change the process name to what version u use

    while True:
        print("https://github.com/XiAnzheng-ID/Terraria-Python-Trainer")
        print("Still Working on other feature")
        print("Feature:")
        print("1. Unlimited Health")
        choice = int(input("Choice?: "))

        if choice == 1:
            subprocess.Popen(["python", "Health.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
            os.system('cls')
        else:
            print("Error , put 1 on the console")
            time.sleep(2)
            os.system('cls')

except ReadWriteMemoryError as error:
    print(error)
    print("Error cant found the process , try run it as administrator")
    print("Does the game running?")
