from ReadWriteMemory import ReadWriteMemory
import Bypass

rwm = ReadWriteMemory()
process = rwm.get_process_by_name("Terraria.exe")
process.open()
base = Bypass.base_address

baseHealth = base + 0x8D1354
health1 = process.get_pointer(baseHealth, offsets=[0x408, 0x14, 0x38 ,0x24, 0x120, 0x20, 0x408])
health2 = process.get_pointer(baseHealth, offsets=[0x408, 0x64, 0x38 ,0x24, 0x120, 0x20, 0x408])
health3 = process.get_pointer(baseHealth, offsets=[0x408, 0x14, 0x3C ,0x24, 0x120, 0x20, 0x408])
health4 = process.get_pointer(baseHealth, offsets=[0x408, 0x64, 0x3C ,0x24, 0x120, 0x20, 0x408])
health5 = process.get_pointer(baseHealth, offsets=[0x408, 0x14, 0x38 ,0x24, 0x110, 0x64, 0x408])
health6 = process.get_pointer(baseHealth, offsets=[0x408, 0x64, 0x38 ,0x24, 0x110, 0x64, 0x408])
health7 = process.get_pointer(baseHealth, offsets=[0x408, 0x14, 0x3C ,0x24, 0x110, 0x64, 0x408])
health8 = process.get_pointer(baseHealth, offsets=[0x408, 0x64, 0x3C ,0x24, 0x110, 0x64, 0x408])