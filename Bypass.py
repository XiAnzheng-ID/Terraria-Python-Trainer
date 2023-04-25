import win32api
import win32con
import win32process

def get_base_address(process_name):
    for pid in win32process.EnumProcesses():
        try:
            handle = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, False, pid)
            exe_path = win32process.GetModuleFileNameEx(handle, 0)
            if process_name in exe_path:
                base_address = win32process.EnumProcessModules(handle)[0]
                return base_address
        except:
            pass
    return None

# Example usage:
base_address = get_base_address("Terraria.exe") #change the process name
if base_address is not None:
    print(f"ASLR bypassed :D Your Base Address is:\n 0x{hex(base_address)[2:]}")
else:
    print("Failed , Try run as administrator or check if the game is in elavated process")