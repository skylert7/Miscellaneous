import os
import itertools
import random
import time
import subprocess
import ctypes, sys

random_name = list(itertools.permutations('ABCG', 3))
random_name = ''.join(random_name[random.randint(0, 24)])
script_file_path = 'C:/Users/Skyler/Git_Folder/Miscellaneous/GameAutomation/NineDragons/demo.au3'
script_exe_file_path = 'C:/Users/Skyler/Git_Folder/Miscellaneous/GameAutomation/NineDragons/{}.exe'.format(random_name)
au3_exe_file_path = 'C://"Program Files (x86)"/AutoIt3/Aut2Exe/Aut2exe_x64.exe'

compile_command = 'cmd /c {} /in {} /out {} /x64'.format(au3_exe_file_path, script_file_path, script_exe_file_path)
# Create executable with unique name
os.system(compile_command)

# Wait for file to be created
time.sleep(2)

# Run executable
# os.startfile(script_exe_file_path)
run_command = 'cmd /k runas /user:Administrator {}'.format(script_exe_file_path)
# run_command = 'runas /user:Administrator notepad.exe'

password = b'1507\n'
os.system(run_command)

# subprocess.Popen('C:/WINDOWS/system32/notepad.exe', shell=True, stdout=subprocess.PIPE)
