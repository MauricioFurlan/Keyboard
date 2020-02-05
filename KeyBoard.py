import keyboard
import re

recorded = keyboard.record(until='esc')

arquivo = open("Log", "w")
for i in recorded:
  arquivo.write(re.sub(r'KeyboardEvent\(. up\)', "", str(i)).replace("down", "").replace("KeyboardEvent","").replace("(space up)","").replace("(ctrl up)", "").replace("(right shift up)","").replace("(enter )","\n").replace("(enter up)",""))
arquivo.close()

