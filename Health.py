from ReadWriteMemory import ReadWriteMemory
import Offset
import ctypes
import os

ctypes.windll.kernel32.SetConsoleTitleW("Unlimited Health")
os.system('cls')
rwm = ReadWriteMemory()
process = rwm.get_process_by_name("Terraria.exe") #change the process name to what version u use
process.open()

print("Dont Close this window just minimized it")
print("Close it when you want to turn off this feature")

edit = int(input("Max HP?: "))
print("Enjoy, :D")
while True:
    process.write(Offset.health1, edit)    
    process.write(Offset.health2, edit)  
    process.write(Offset.health3, edit)  
    process.write(Offset.health4, edit)  
    process.write(Offset.health5, edit)     
    process.write(Offset.health6, edit)  
    process.write(Offset.health7, edit)  
    process.write(Offset.health8, edit)  